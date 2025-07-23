from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from config import Config
from db import db
from auth import auth_bp
from chat import chat_bp
from goals import goals_bp
from payments import payments_bp

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize extensions
jwt = JWTManager(app)
mail = Mail(app)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(goals_bp)
app.register_blueprint(payments_bp)

# Health check routes
@app.route('/')
def index():
    return {"message": "MindMate Backend Running 🎉"}

@app.route('/ping')
def ping():
    return {"pong": True}

@app.route('/test-db')
def test_db():
    try:
        db.session.execute('SELECT 1')
        return {"db": "Connected successfully ✅"}
    except Exception as e:
        return {"error": str(e)}, 500
