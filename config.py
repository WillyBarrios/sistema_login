import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "contraseña")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://tu-usario:contraseña@localhost/sistemaventa")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "contraseña")