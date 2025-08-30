from flask import Blueprint, render_template, request, redirect, url_for
from app.models.empleado import Empleado
from app import db

empleados_bp = Blueprint("empleados", __name__)

@empleados_bp.route("/empleados")
def listar_empleados():
    empleados = Empleado.query.all()
    return render_template("empleados.html", empleados=empleados)

@empleados_bp.route("/empleados/create", methods=["POST"])
def crear_empleado():
    nombre = request.form.get("nombre")
    if nombre:
        nuevo = Empleado(Nombre=nombre)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("empleados.listar_empleados"))

@empleados_bp.route("/empleados/edit/<int:id>", methods=["GET", "POST"])
def editar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    if request.method == "POST":
        empleado.Nombre = request.form.get("nombre")
        db.session.commit()
        return redirect(url_for("empleados.listar_empleados"))
    return render_template("editar_empleado.html", empleado=empleado)

@empleados_bp.route("/empleados/delete/<int:id>")
def eliminar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for("empleados.listar_empleados"))
