from flask import Flask
from flask_restful import Api
from connection import WarehouseConnections
from generic import set_generic_calls
from service_endpoints import set_service_calls


app = Flask(__name__)
api = Api(app)
db = WarehouseConnections()
set_generic_calls(api)
set_service_calls(api)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
