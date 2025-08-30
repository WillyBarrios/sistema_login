from flask import Blueprint, render_template, request, redirect, url_for
from app.models.producto import Producto
from app import db

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/productos")
def listar_productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos=productos)

@productos_bp.route("/productos/create", methods=["POST"])
def crear_producto():
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    cantidad = request.form.get("cantidad_disponible")
    if nombre and precio is not None and cantidad is not None:
        nuevo = Producto(
            Nombre=nombre,
            Precio=float(precio),
            Cantidad_Disponible=int(cantidad)
        )
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("productos.listar_productos"))

@productos_bp.route("/productos/edit/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if request.method == "POST":
        producto.Nombre = request.form.get("nombre")
        producto.Precio = float(request.form.get("precio"))
        producto.Cantidad_Disponible = int(request.form.get("cantidad_disponible"))
        db.session.commit()
        return redirect(url_for("productos.listar_productos"))
    return render_template("editar_producto.html", producto=producto)

@productos_bp.route("/productos/delete/<int:id>")
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for("productos.listar_productos"))
