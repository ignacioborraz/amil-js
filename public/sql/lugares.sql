CREATE TABLE lugares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lugar VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    ciudad VARCHAR(100) NOT NULL
);

INSERT INTO lugares (lugar, direccion, ciudad) VALUES
('Mandarine Tent', 'Av. Costanera Norte y Sarmiento', 'CABA'),
('Crobar', 'Av. Coronel Marcelino E. Freyre 3832', 'CABA'),
('Studio Theater', 'Rosario de Sta. Fe 272', 'Córdoba'),
('Blue Velvet', 'Av. Carlos Colombres 1698', 'Rosario'),
('Club Morocco', 'CJH4+9F', 'CABA'),
('Forja', 'Mauricio Yadarola 1699', 'Córdoba'),
('Metropolitano', 'Junín 501', 'Rosario'),
('Quinta Las Rosas', 'Cjón. Escorhiuela 2301', 'Mendoza'),
('Parque Sarmiento', 'Av. Dr. Ricardo Balbín 4750', 'CABA'),
('Movistar Arena', 'Humboldt 450', 'CABA');
