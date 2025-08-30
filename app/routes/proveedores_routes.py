from flask import Blueprint, render_template, request, redirect, url_for
from app.models.proveedor import Proveedor
from app import db

proveedores_bp = Blueprint("proveedores", __name__)

@proveedores_bp.route("/proveedores")
def listar_proveedores():
    proveedores = Proveedor.query.all()
    return render_template("proveedores.html", proveedores=proveedores)

@proveedores_bp.route("/proveedores/create", methods=["POST"])
def crear_proveedor():
    nombre = request.form.get("nombre")
    if nombre:
        nuevo = Proveedor(Nombre=nombre)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("proveedores.listar_proveedores"))

@proveedores_bp.route("/proveedores/edit/<int:id>", methods=["GET", "POST"])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    if request.method == "POST":
        proveedor.Nombre = request.form.get("nombre")
        db.session.commit()
        return redirect(url_for("proveedores.listar_proveedores"))
    return render_template("editar_proveedor.html", proveedor=proveedor)

@proveedores_bp.route("/proveedores/delete/<int:id>")
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for("proveedores.listar_proveedores"))
