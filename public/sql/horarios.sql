CREATE TABLE horarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    desde VARCHAR(10) NOT NULL,
    hasta VARCHAR(10) NOT NULL,
    artista_id INT NOT NULL,
    FOREIGN KEY (artista_id) REFERENCES artistas(id)
);

INSERT INTO horarios (desde, hasta, artista_id) VALUES
('17:00', '20:00', 1),
('20:00', '23:59', 2);
