from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.clientes_controller import (
    get_all_clientes,
    create_cliente,
    get_cliente_by_id,
    update_cliente,
    delete_cliente
)

clientes_bp = Blueprint("clientes", __name__)

@clientes_bp.route("/clientes")
def listar_clientes():
    clientes = get_all_clientes()
    return render_template("clientes.html", clientes=clientes)

@clientes_bp.route("/clientes/create", methods=["POST"])
def crear_cliente():
    nombre = request.form.get("nombre")
    if nombre:
        create_cliente(nombre)
    return redirect(url_for("clientes.listar_clientes"))

@clientes_bp.route("/clientes/edit/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    cliente = get_cliente_by_id(id)
    if request.method == "POST":
        nombre = request.form.get("nombre")
        update_cliente(id, nombre)
        return redirect(url_for("clientes.listar_clientes"))
    return render_template("editar_cliente.html", cliente=cliente)

@clientes_bp.route("/clientes/delete/<int:id>")
def eliminar_cliente(id):
    delete_cliente(id)
    return redirect(url_for("clientes.listar_clientes"))
