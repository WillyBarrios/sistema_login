from flask import Blueprint, render_template, request, redirect, url_for
from app.models.usuario import Usuario
from app import db, bcrypt
from app.models.roles import Rol

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()
    roles = Rol.query.all()
    return render_template("usuarios.html", usuarios=usuarios, roles=roles)

@usuarios_bp.route("/usuarios/create", methods=["POST"])
def crear_usuario():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    contraseña = request.form.get("contraseña")
    id_rol = request.form.get("ID_Rol")
    if nombre and correo and contraseña and id_rol:
        hash_pw = bcrypt.generate_password_hash(contraseña).decode('utf-8')
        nuevo = Usuario(Nombre=nombre, Correo=correo, Contraseña=hash_pw, ID_Rol=id_rol)
        db.session.add(nuevo)
        db.session.commit()
    return redirect(url_for("usuarios.listar_usuarios"))

@usuarios_bp.route("/usuarios/edit/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == "POST":
        usuario.Nombre = request.form.get("nombre")
        usuario.Correo = request.form.get("correo")
        nueva_contraseña = request.form.get("contraseña")
        if nueva_contraseña:
            usuario.Contraseña = bcrypt.generate_password_hash(nueva_contraseña).decode('utf-8')
        db.session.commit()
        return redirect(url_for("usuarios.listar_usuarios"))
    return render_template("editar_usuario.html", usuario=usuario)

@usuarios_bp.route("/usuarios/delete/<int:id>")
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for("usuarios.listar_usuarios"))
