# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

import pymysql
pymysql.install_as_MySQLdb()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from app.routes.rol_permiso_routes import rol_permiso_bp
    app.register_blueprint(rol_permiso_bp)
    from app.routes.permisos_routes import permisos_bp
    app.register_blueprint(permisos_bp)
    from app.routes.roles_routes import roles_bp
    app.register_blueprint(roles_bp)
    from app.routes.usuarios_routes import usuarios_bp
    app.register_blueprint(usuarios_bp)
    from app.routes.productos_routes import productos_bp
    app.register_blueprint(productos_bp)
    from app.routes.empleados_routes import empleados_bp
    app.register_blueprint(empleados_bp)
    from app.routes.proveedores_routes import proveedores_bp
    app.register_blueprint(proveedores_bp)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    # Importar modelos para que SQLAlchemy los registre
    from app.models import roles


    # Importar y registrar rutas
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.routes.clientes_routes import clientes_bp
    app.register_blueprint(clientes_bp)

    @app.route("/")
    def root():
        from flask import redirect, url_for
        return redirect(url_for('auth.login'))

    return app