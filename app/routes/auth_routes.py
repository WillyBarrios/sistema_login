from flask import Blueprint, app, render_template, request, jsonify, redirect, url_for, session
from app.models.usuario import Usuario
from app.models.empleado import Empleado
from app.models.producto import Producto
from app.models.proveedor import Proveedor
from app.models.cliente import Cliente
from app import db, bcrypt
from flask_jwt_extended import create_access_token

from flask import Blueprint, app, render_template, request, jsonify, redirect, url_for, session

auth_bp = Blueprint("auth", __name__)

# Ruta para cerrar sesión
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # POST: procesar login
    data = request.form if request.form else request.get_json()
    correo = data.get("correo")
    contraseña = data.get("contraseña")
    usuario = Usuario.query.filter_by(Correo=correo).first()
    if usuario:
        print(f"Hash en BD: {usuario.Contraseña}")
        print(f"Contraseña ingresada: {contraseña}")
        print(f"Resultado bcrypt: {bcrypt.check_password_hash(usuario.Contraseña, contraseña)}")
        # Guardar el nombre del rol y usuario en la sesión
        from app.models.roles import Rol
        rol = Rol.query.get(usuario.ID_Rol)
        session['rol'] = rol.Nombre if rol else None
        session['usuario'] = usuario.Nombre if usuario.Nombre else usuario.Correo
    bcrypt_result = False
    hash_bd = None
    if usuario:
        hash_bd = usuario.Contraseña
        bcrypt_result = bcrypt.check_password_hash(usuario.Contraseña, contraseña)
    if not usuario or not bcrypt_result:
        return render_template(
            "login.html",
            error="Credenciales inválidas",
            hash_bd=hash_bd,
            pass_ingresada=contraseña,
            bcrypt_result=bcrypt_result
        )
    token = create_access_token(identity=usuario.ID_usuario)
    return redirect(url_for("auth.dashboard"))
@auth_bp.route("/dashboard")
def dashboard():
    total_empleados = Empleado.query.count()
    total_productos = Producto.query.count()
    total_proveedores = Proveedor.query.count()
    total_clientes = Cliente.query.count()
    dashboard_data = [total_empleados, total_productos, total_proveedores, total_clientes]
    return render_template(
        "dashboard.html",
        total_empleados=total_empleados,
        total_productos=total_productos,
        total_proveedores=total_proveedores,
        total_clientes=total_clientes,
        dashboard_data=dashboard_data,
        usuario=session.get('usuario'),
        rol=session.get('rol')
    )

@auth_bp.route("/")
def index():
    return render_template("login.html")