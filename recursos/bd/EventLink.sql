-- Creación de la Base de Datos (ej. en PostgreSQL o MySQL)
-- CREATE DATABASE EventLinkDB;

-- 1. Tabla de Roles
CREATE TABLE Rol (
    id_rol INT PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE -- Ej: 'Administrador', 'Cliente', 'Afiliado'
);

-- 2. Tabla de Usuarios (para Clientes, Organizadores Afiliados y Administradores)
CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL, -- Almacenamiento seguro del hash
    rol_id INT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Datos específicos de organizador / cliente pueden ir aquí o en tablas separadas
    nombre_empresa VARCHAR(150), -- Solo para Afiliado
    rtn VARCHAR(20),             -- Solo para Afiliado
    telefono VARCHAR(20),        -- Para Cliente/Afiliado
    
    FOREIGN KEY (rol_id) REFERENCES Rol(id_rol)
);

-- 3. Tabla de Categorias de Eventos
CREATE TABLE Categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- 4. Tabla de Eventos
CREATE TABLE Evento (
    id_evento SERIAL PRIMARY KEY,
    organizador_id INT NOT NULL,
    categoria_id INT NOT NULL,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    fecha_hora TIMESTAMP NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    estado VARCHAR(50) DEFAULT 'Activo', -- Ej: 'Activo', 'Pendiente', 'Cancelado', 'Finalizado'
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (organizador_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id_categoria)
);

-- 5. Tabla de Tipos de Entradas (ej. VIP, General, Preventa)
CREATE TABLE TipoEntrada (
    id_tipo_entrada SERIAL PRIMARY KEY,
    evento_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    cantidad_total INT NOT NULL,
    cantidad_disponible INT NOT NULL,

    FOREIGN KEY (evento_id) REFERENCES Evento(id_evento)
);

-- 6. Tabla de Compras
CREATE TABLE Compra (
    id_compra SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    estado_pago VARCHAR(50) NOT NULL, -- Ej: 'Pendiente', 'Confirmado', 'Fallido'

    FOREIGN KEY (cliente_id) REFERENCES Usuario(id_usuario)
);

-- 7. Tabla de Transacciones de Pago (registro detallado)
CREATE TABLE TransaccionPago (
    id_transaccion SERIAL PRIMARY KEY,
    compra_id INT UNIQUE NOT NULL, -- Una transacción por compra
    monto DECIMAL(10, 2) NOT NULL,
    metodo_pago VARCHAR(50), -- Ej: 'Tarjeta Crédito', 'PayPal'
    referencia_externa VARCHAR(100), -- ID de la pasarela de pago
    fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (compra_id) REFERENCES Compra(id_compra)
);

-- 8. Tabla de Detalle de Compra (para la relación N:M entre Compra y TipoEntrada)
CREATE TABLE DetalleCompra (
    id_detalle SERIAL PRIMARY KEY,
    compra_id INT NOT NULL,
    tipo_entrada_id INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10, 2) NOT NULL,
    
    FOREIGN KEY (compra_id) REFERENCES Compra(id_compra),
    FOREIGN KEY (tipo_entrada_id) REFERENCES TipoEntrada(id_tipo_entrada)
);