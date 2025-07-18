from flask_mysqldb import MySQL

def init_mysql(app):
    return MySQL(app)
