from flask import Blueprint, render_template, request, redirect, url_for
from app.models.roles import Rol
from app import db

roles_bp = Blueprint("roles", __name__)

@roles_bp.route("/roles")
def listar_roles():
    roles = Rol.query.all()
    return render_template("roles.html", roles=roles)

@roles_bp.route("/roles/create", methods=["POST"])
def crear_rol():
    nombre = request.form.get("nombre")
    if nombre:
        nuevo = Rol(Nombre=nombre)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("roles.listar_roles"))

@roles_bp.route("/roles/edit/<int:id>", methods=["GET", "POST"])
def editar_rol(id):
    rol = Rol.query.get_or_404(id)
    if request.method == "POST":
        rol.Nombre = request.form.get("nombre")
        db.session.commit()
        return redirect(url_for("roles.listar_roles"))
    return render_template("editar_rol.html", rol=rol)

@roles_bp.route("/roles/delete/<int:id>")
def eliminar_rol(id):
    rol = Rol.query.get_or_404(id)
    db.session.delete(rol)
    db.session.commit()
    return redirect(url_for("roles.listar_roles"))
