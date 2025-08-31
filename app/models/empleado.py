from app import db

class Empleado(db.Model):
    __tablename__ = "empleados"
    ID_Empleado = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
