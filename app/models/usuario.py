from app import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    ID_usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100))
    Correo = db.Column(db.String(100), unique=True)
    Contraseña = db.Column(db.String(100))
    ID_Rol = db.Column(db.Integer, db.ForeignKey("roles.ID_Rol"))