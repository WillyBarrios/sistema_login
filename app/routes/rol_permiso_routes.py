from flask import Blueprint, render_template, request, redirect, url_for
from app.models.rol_permiso import RolPermiso
from app.models.roles import Rol
from app.models.permiso import Permiso
from app import db

rol_permiso_bp = Blueprint("rol_permiso", __name__)

@rol_permiso_bp.route("/rol_permiso")
def listar_rol_permisos():
    rol_permisos = RolPermiso.query.all()
    # Cargar los nombres de rol y permiso
    for rp in rol_permisos:
        rp.rol = Rol.query.get(rp.ID_Rol)
        rp.permiso = Permiso.query.get(rp.ID_Permiso)
    roles = Rol.query.all()
    permisos = Permiso.query.all()
    return render_template("rol_permiso.html", rol_permisos=rol_permisos, roles=roles, permisos=permisos)

@rol_permiso_bp.route("/rol_permiso/asignar", methods=["POST"])
def asignar_permiso():
    id_rol = request.form.get("id_rol")
    id_permiso = request.form.get("id_permiso")
    if id_rol and id_permiso:
        nuevo = RolPermiso(ID_Rol=id_rol, ID_Permiso=id_permiso)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("rol_permiso.listar_rol_permisos"))

@rol_permiso_bp.route("/rol_permiso/delete/<int:id_rol_permiso>")
def quitar_permiso(id_rol_permiso):
    rp = RolPermiso.query.get_or_404(id_rol_permiso)
    db.session.delete(rp)
    db.session.commit()
    return redirect(url_for("rol_permiso.listar_rol_permisos"))
