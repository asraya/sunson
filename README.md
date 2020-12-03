# PT Sunson

''
# Frontend (vuejs-frontend) 
How to run:
cd vuejs-frontend

Install dependency
```sh
$ npm install
```
Run app
```sh
$ npm run dev
```
Server run in http://localhost:8080

# Backend (flask-backend)
How to run:
cd flask-backend
Installing virtual environment
```sh
$ virtualenv -p python3 venv
```
Load environment
```sh
$ source venv/bin/activate
```
Installing dependency
```sh
$ pip install -r requirements.txt
```
For first time instalation, create database if not exist
```sh
$ python
>>> from employee import db
>>> db.create_all()
>>> exit()
```

Run app
```sh
$ python employee.py
```
Server run in http://localhost:5000

# Unit Test
This unit test only for *flask-backend*. Run it from 'flask-backend' folder.
```sh
$ python test/employee_test.py
```
