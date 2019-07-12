from flask_restful import Resource


class Marco(Resource):
    def get(self):
        return {'message': 'pollo'}


def set_generic_calls(api):
    api.add_resource(Marco, '/marco')
    return api
