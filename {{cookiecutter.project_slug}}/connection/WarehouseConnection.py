from sqlalchemy import create_engine


class WarehouseConnections:

    engine_connection_string = 'mssql+pymssql://{{cookiecutter.db_user}}:{{cookiecutter.db_pass}}@{{cookiecutter.db_server}}/%s'
    databases = ['DepartmentalDataMart', 'Metadata', 'Operations', 'PollingStaging', 'TransactionMart', 'Warehouse']

    def __init__(self):
        self.engines = dict()

        for database in self.databases:
            self.engines[database] = create_engine(self.engine_connection_string % database)

    def get_engine(self, key):
        if key in self.engines:
            return self.engines[key]
        else:
            raise Exception('Specific Engine: %s not found' % key)

