from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import Config
from db import init_mysql
from auth import auth_bp
from chat import chat_bp
from goals import goals_bp
from payments import payments_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

jwt = JWTManager(app)
mail = Mail(app)
mysql = init_mysql(app)
app.mysql = mysql

app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(goals_bp)
app.register_blueprint(payments_bp)

@app.route('/')
def index():
    return {"message": "MindMate Backend Running"}

if __name__ == '__main__':
    app.run(debug=True)
