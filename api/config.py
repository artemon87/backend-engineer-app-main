class DevelopmentConfig():
    """
    Development configurations will go here
    """
    DEBUG = True

class GlobalConfig:
    __conf = {
        "GLOBAL.flask_port": 4000,
        "GLOBAL.flask_host": "127.0.0.1",
        "GLOBAL.db_name" :   "employees.db",
        "GLOBAL.db_table_name" : "employees",
    }

    @staticmethod
    def config(name):
        if name in GlobalConfig.__conf:
            return GlobalConfig.__conf.get(name)
        return None
