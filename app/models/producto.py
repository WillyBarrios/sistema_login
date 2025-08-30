from app import db

class Producto(db.Model):
    __tablename__ = "productos"
    ID_Producto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Precio = db.Column(db.Float)
    Cantidad_Disponible = db.Column(db.Integer)
