CREATE TABLE generos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genero VARCHAR(255) NOT NULL,
    descripcion TEXT
);

INSERT INTO generos (genero, descripcion) VALUES
('Trance', 'Un género de música electrónica de ritmo rápido, con un enfoque en melodías atmosféricas.'),
('Trance progresivo', 'Una subcategoría de trance con énfasis en la progresión y evolución de los sonidos.'),
('Vocal trance', 'Trance que incluye vocales prominentes en sus pistas.'),
('Electro house', 'Un estilo de house con influencias de música electro.'),
('House', 'Un género de música electrónica bailable originado en la década de 1980.'),
('Tecno', 'Un género de música electrónica centrado en ritmos repetitivos y sonidos sintéticos.'),
('Uplifting Trance', 'Una variante de trance conocida por sus melodías alegres y energéticas.'),
('Chill Out', 'Música electrónica relajante y atmosférica.'),
('Dance Music', 'Música electrónica diseñada para ser bailada.'),
('EDM', 'Electronic Dance Music, un término amplio que engloba varios géneros de música electrónica bailable.'),
('Progressive House', 'Una subcategoría de house con un enfoque en la evolución gradual de los elementos sonoros.'),
('Melodic Deep', 'Un estilo de música electrónica que combina elementos melódicos y profundos.'),
('Big Room House', 'Un subgénero de house caracterizado por su sonido expansivo y pensado para grandes eventos.'),
('Deep House', 'Un estilo de house con influencias de jazz, soul y funk.'),
('Tech House', 'Una mezcla de techno y house.'),
('Electro Hop', 'Un género que combina elementos de electro y hip-hop.'),
('Minimal Techno', 'Un subgénero de techno centrado en la simplicidad y repetición.'),
('Techno', 'Un género de música electrónica caracterizado por ritmos repetitivos y sonidos sintéticos.'),
('Melodic Techno', 'Un estilo de techno con un enfoque en melodías.'),
('Progressive', 'Un término general para la música electrónica que enfatiza la evolución y la progresión.'),
('Psico Trance', 'Una variante de trance con elementos psicodélicos.');

