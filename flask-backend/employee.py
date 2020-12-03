from flask import Flask, request, jsonify, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_cors import CORS
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'employee.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_employee = db.Column(db.String(1000), unique=True)
    division = db.Column(db.String(1000))
    thumbnail = db.Column(db.String(1000))
    date_updated = db.Column(db.DateTime, nullable=False,
                    default=datetime.now())
    date_created = db.Column(db.DateTime, nullable=False,
                    default=datetime.now())

    def __init__(self, name_employee, division, thumbnail, date_updated, date_created):
        self.name_employee = name_employee
        self.division = division
        self.thumbnail = thumbnail
        self.date_updated = date_updated
        self.date_created = date_created

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name_employee', 'division', 'thumbnail', 'date_updated', 'date_created')


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def message_fail(message):
    return json.dumps({'success': False, 'message': message}), 200, {'DivisionType': 'application/json'}

# get images
@app.route("/images/<name>", methods=["GET"])
def get_image(name):
    path = os.getcwd() + '/images/'
    if os.path.isfile(path + name):
       filename = path + name
    else:
       filename = path + 'error.jpeg'
    return send_file(filename, mimetype='image/jpeg')

# upload image
def upload_image(data):
    if 'file' not in data:
        message_fail('No file uploaded')
    file = data['file']
    if file.filename == '':
        message_fail('File doesnt have name!')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'http://' + request.host + '/images/' + filename

# endpoint to create new 
@app.route("/employee", methods=["POST"])
def add_employee():
    name_employee = request.form['name_employee']
    division = request.form['division']
    thumbnail = upload_image(request.files)
    date_updated = datetime.now()
    date_created = datetime.now()
    new_employee = Employee(name_employee, division, thumbnail, date_updated, date_created)

    db.session.add(new_employee)
    db.session.commit()

    return json.dumps({'success': True, 'message': 'Data has been saved'}), 200, {'DivisionType': 'application/json'}

# endpoint to show all 
@app.route("/employee", methods=["GET"])
def get_employee():
    all_employees = Employee.query.all()
    result = employees_schema.dump(all_employees)
    return jsonify(result.data)

# endpoint to get employee detail by id
@app.route("/employee/<id>", methods=["GET"])
def employee_detail(id):
    employee = Employee.query.get(id)
    return employee_schema.jsonify(employee)


# endpoint to update 
@app.route("/employee/<id>", methods=["PUT", "PATCH"])
def employee_update(id):
    employee = Employee.query.get(id)
    employee.name_employee = request.form['name_employee'] if 'name_employee' in request.form else employee.name_employee
    employee.division = request.form['division'] if 'division' in request.form else employee.division
    employee.thumbnail = upload_image(request.files) if 'file' in request.files else employee.thumbnail
    employee.date_updated = datetime.now()
    employee.date_created = employee.date_created
    
    db.session.commit()
    return employee_schema.jsonify(employee)


# endpoint to delete 
@app.route("/employee/<id>", methods=["DELETE"])
def employee_delete(id):
    employee = Employee.query.get(id)
    status = db.session.delete(employee)
    db.session.commit()

    if status == None:
        os.remove(os.getcwd() + '/images/' + employee.thumbnail.split('/')[-1])
    return employee_schema.jsonify(employee)


if __name__ == '__main__':
    app.run(debug=True)
