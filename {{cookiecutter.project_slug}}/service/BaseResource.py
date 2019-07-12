from flask_restful import Resource, reqparse
from sqlalchemy.orm import sessionmaker
from connection import WarehouseConnections, AlchemyEncoder
import json


class BaseResource(Resource):

    def __parse_args(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()

    def get(self):
        return {"message": 'New Phone, Who dis?'}
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class ServiceBase:

    def __init__(self, store_num=None):
        db = WarehouseConnections()
        self.store_num = store_num
        session = sessionmaker(db.get_engine('{{cookiecutter.db_name}}'), autocommit=True)
        self.session = session()

    def get_response(self):
        return
