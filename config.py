import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "Aa12345678")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://wbarrios:Aa12345678@localhost/sistemaventa")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "Aa12345678")