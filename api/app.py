from flask import Flask
from flask_restful import Api
from config import GlobalConfig
from resource import EmployeesResource



app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)

"""
Endpoints
"""
api.add_resource(EmployeesResource, '/employees')

if __name__ == '__main__':
    app.run(host = GlobalConfig.config("GLOBAL.flask_host"), 
            port = GlobalConfig.config("GLOBAL.flask_port"))