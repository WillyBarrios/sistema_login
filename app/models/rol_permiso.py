from app import db

class RolPermiso(db.Model):
    __tablename__ = "rol_permiso"
    ID_Rol_Permiso = db.Column(db.Integer, primary_key=True)
    ID_Rol = db.Column(db.Integer, db.ForeignKey("roles.ID_Rol"))
    ID_Permiso = db.Column(db.Integer, db.ForeignKey("permisos.ID_Permiso"))
