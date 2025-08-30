from flask import Blueprint, render_template, request, redirect, url_for
from app.models.permiso import Permiso
from app import db

permisos_bp = Blueprint("permisos", __name__)

@permisos_bp.route("/permisos")
def listar_permisos():
    permisos = Permiso.query.all()
    return render_template("permisos.html", permisos=permisos)

@permisos_bp.route("/permisos/create", methods=["POST"])
def crear_permiso():
    nombre = request.form.get("nombre")
    if nombre:
        nuevo = Permiso(Nombre=nombre)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("permisos.listar_permisos"))

@permisos_bp.route("/permisos/edit/<int:id>", methods=["GET", "POST"])
def editar_permiso(id):
    permiso = Permiso.query.get_or_404(id)
    if request.method == "POST":
        permiso.Nombre = request.form.get("nombre")
        db.session.commit()
        return redirect(url_for("permisos.listar_permisos"))
    return render_template("editar_permiso.html", permiso=permiso)

@permisos_bp.route("/permisos/delete/<int:id>")
def eliminar_permiso(id):
    permiso = Permiso.query.get_or_404(id)
    db.session.delete(permiso)
    db.session.commit()
    return redirect(url_for("permisos.listar_permisos"))
