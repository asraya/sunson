 
 
import os
import unittest
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from employee import *

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
 

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
  
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
      
    def tearDown(self):
        pass
 
 
    def test_main_page(self):
        response = self.app.get('/employee', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_page(self, id="1"):
        response = self.app.get('/employee/'+id, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()