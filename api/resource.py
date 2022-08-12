from models import loadSession, Employees
from flask import request, jsonify
from flask_restful import Resource



class EmployeesResource(Resource):

    def __init__(self):
        pass

    def get(self):
        """
        GET method
        """
        session = loadSession()
        data = [i.export_data() for i in session.query(Employees).all()]
        session.close()
        return jsonify(data)
        

