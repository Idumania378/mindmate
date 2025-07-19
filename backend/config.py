class Config:
    SECRET_KEY = "super-secret"
    SQLALCHEMY_DATABASE_URI = "mysql://root:MHuHjFkvDBNAscawowjlVishPXpfdyvj@mysql.railway.internal:3306/railway"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-jwt"

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your-email@gmail.com"
    MAIL_PASSWORD = "your-gmail-app-password"
