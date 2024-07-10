CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dia INT NOT NULL,
    mes VARCHAR(10) NOT NULL,
    anio INT NOT NULL,
    inicio VARCHAR(10) NOT NULL,
    cierre VARCHAR(10) NOT NULL,
    lugar_id INT NOT NULL,
    FOREIGN KEY (lugar_id) REFERENCES lugares(id),
    artista_id INT NOT NULL,
    FOREIGN KEY (artista_id) REFERENCES artistas(id),
    entrada_id INT NOT NULL,
    FOREIGN KEY (entrada_id) REFERENCES entradas(id),
    horario_id INT NOT NULL,
    FOREIGN KEY (horario_id) REFERENCES horarios(id)
);

INSERT INTO eventos (dia, mes, anio, inicio, cierre, lugar_id, artista_id, entrada_id, horario_id) VALUES
(11, 'Mayo', 2024, '17:00', '23:59', 1, 1, 1, 1),
(24, 'Mayo', 2024, '21:00', '05:00', 2, 2, 1, 1),
(25, 'Mayo', 2024, '23:00', '06:00', 3, 3, 1, 1),
(8, 'Junio', 2024, '23:00', '06:00', 1, 1, 1, 1),
(15, 'Junio', 2024, '23:00', '06:00', 4, 4, 1, 1),
(16, 'Junio', 2024, '23:00', '06:00', 4, 4, 1, 1),
(19, 'Junio', 2024, '23:00', '05:00', 5, 5, 1, 1),
(5, 'Julio', 2024, '22:00', '05:00', 6, 6, 1, 1),
(6, 'Julio', 2024, '23:00', '06:00', 1, 1, 1, 1),
(19, 'Julio', 2024, '21:00', '06:00', 7, 7, 1, 1),
(20, 'Julio', 2024, '21:00', '05:00', 2, 2, 1, 1),
(21, 'Sept.', 2024, '22:00', '07:00', 1, 1, 1, 1),
(11, 'Octubre', 2024, '23:00', '06:00', 8, 8, 1, 1),
(12, 'Octubre', 2024, '22:00', '06:00', 9, 9, 1, 1),
(12, 'Octubre', 2024, '23:00', '07:00', 10, 10, 1, 1);
