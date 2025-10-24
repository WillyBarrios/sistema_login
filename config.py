import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "Aa12345678")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://wbarrios:Aa12345678@localhost:3306/sistemaventa?charset=utf8mb4")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'connect_args': {
            'connect_timeout': 60,
            'read_timeout': 60,
            'write_timeout': 60
        }
    }
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "Aa12345678")