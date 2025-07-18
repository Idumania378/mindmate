import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if present

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "super-secret")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-jwt")
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # your Gmail address
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # your App Password
