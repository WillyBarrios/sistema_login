from app import db

class Rol(db.Model):
    __tablename__ = "roles"
    ID_Rol = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))