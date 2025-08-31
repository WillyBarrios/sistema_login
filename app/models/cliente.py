from app import db

class Cliente(db.Model):
    __tablename__ = "clientes"
    ID_Cliente = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
   
