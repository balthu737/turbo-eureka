CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id BIGINT NOT NULL UNIQUE,
    nombre VARCHAR(100),
    username VARCHAR(100),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario_id BIGINT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);

CREATE TABLE movimiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    monto DECIMAL(10,2),
    categoria_id INT,
    usuario_id BIGINT,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);
