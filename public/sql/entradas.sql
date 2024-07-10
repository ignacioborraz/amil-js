CREATE TABLE entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL
);

INSERT INTO entradas (tipo, precio, cantidad) VALUES
('early', 20000.00, 20000),
('general', 30000.00, 40000),
('vip', 50000.00, 10000),
('backstage', 100000.00, 2000);