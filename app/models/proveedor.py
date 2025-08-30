from app import db

class Proveedor(db.Model):
    __tablename__ = "proveedores"
    ID_Proveedor = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    # Puedes agregar más campos según tu modelo real
