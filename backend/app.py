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

CORS(app)

jwt = JWTManager(app)
mail = Mail(app)

# Initialize DB
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(goals_bp)
app.register_blueprint(payments_bp)

@app.route('/')
def index():
    return {"message": "MindMate Backend Running"}

@app.route('/test-db')
def test_db():
    try:
        db.session.execute('SELECT 1')
        return {"db": "Connected successfully ✅"}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


