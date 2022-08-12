import requests
from api.config import GlobalConfig
from unittest import TestCase, main
from api.models import Employees, loadSession



class TestEmployeeAPI(TestCase):
    def setUp(self):
        server_ip = GlobalConfig.config("GLOBAL.flask_host")
        server_port = GlobalConfig.config("GLOBAL.flask_port")
        self.requests_session = requests.Session()
        self.requests_session.headers.update({'content-type': 'application/json'})
        self.url = 'http://{}:{}/employees'.format(server_ip, server_port)
        self.db_session = loadSession()
        
        
    def tearDown(self):
        self.db_session.close()


    def test_employee_endpoint(self):
        response = self.requests_session.get(self.url, timeout = (1, 1))
        assert response.status_code == 200
        assert response.request.url == self.url 
        assert response.json() == [emp.export_data() for emp in self.db_session.query(Employees).all()]
        

if __name__ == "__main__":
    main()