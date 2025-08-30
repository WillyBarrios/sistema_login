from app import db

class Permiso(db.Model):
    __tablename__ = "permisos"
    ID_Permiso = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
