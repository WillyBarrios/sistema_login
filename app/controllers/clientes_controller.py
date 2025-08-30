from app.models.cliente import Cliente
from app import db

def get_all_clientes():
    return Cliente.query.all()

def create_cliente(nombre):
    nuevo = Cliente(Nombre=nombre)
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def get_cliente_by_id(id):
    return Cliente.query.get_or_404(id)

def update_cliente(id, nombre):
    cliente = get_cliente_by_id(id)
    cliente.Nombre = nombre
    db.session.commit()
    return cliente

def delete_cliente(id):
    cliente = get_cliente_by_id(id)
    db.session.delete(cliente)
    db.session.commit()
