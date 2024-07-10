CREATE TABLE artistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    artista VARCHAR(255) NOT NULL,
    imagen VARCHAR(255),
    avatar VARCHAR(255),
    foto VARCHAR(255),
    video TEXT,
    origen VARCHAR(255),
    nacionalidad VARCHAR(255),
    descripcion TEXT,
    genero_id INT,
    FOREIGN KEY (genero_id) REFERENCES generos(id)
);

INSERT INTO artistas (artista, origen, nacionalidad, descripcion, avatar, foto, imagen, video) VALUES
('Above & Beyond', 'Londres, Reino Unido', 'inglés', 'Above & Beyond es un reconocido y prestigioso trío británico de Productores, Músicos y DJs de los géneros Trance, Progressive, Downtempo y Alternative formado en 2000 por Jonathan "Jono" Grant, Tony McGuinness y Paavo Siljamäki. El grupo ha sido nominado a los premios Grammy dos veces y ha adquirido gran fama y un alto renombre mundial por sus destacadas producciones, conciertos acústicos y colaboraciones con varios vocalistas, además de ser reconocidos por celebridades por fuera de la escena de la música electrónica, como Madonna, Dido, Radiohead, Coldplay, Miguel Bosé y Britney Spears debido a sus colaboraciones y remixes oficiales.', 'https://i.postimg.cc/cHmWkGM9/aboveandbeyond.jpg', 'https://i.postimg.cc/GtgCrPfv/above.avif', 'https://i.postimg.cc/GtgCrPfv/above.avif', '<iframe class="h-video" src="https://www.youtube.com/embed/MEzU1HvBo6Y?si=eNHGcEKt4_e0P0Xu\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Adriatique', 'Zúrich, Suiza', 'suizo', 'Adriatique es un dúo de DJs suizo conformado por Adrian Shala y Adrian Schweizer. Varían entre el techno y el house, con aires minimalistas, estilo melódico profundo y ritmo sutil e hipnótico.', 'https://i.postimg.cc/h4s4pT2D/adriatique-avatar.jpg', 'https://i.postimg.cc/59s1w1tj/Adriatique.jpg', 'https://i.postimg.cc/59s1w1tj/Adriatique.jpg', '<iframe class="h-video" src="https://www.youtube.com/embed/w4LRUBFy3pc?si=-ZCsSoxEkkUM5THQ\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Aly & Fila', 'El Cairo, Egipto', 'egipciano', 'Aly & Fila es un dúo egipcio de DJs y productores de música trance, formado por Aly Amr Fathalah (Aly) y Fadi Wassef Naguib (Fila), ambos nacidos en 1981. Eran amigos desde la infancia, pero no fue hasta después de enamorarse de la música de Paul van Dyk cuando decidieron construir su primer estudio y empezar a hacer su propia música, a partir de 1999.', 'https://i.postimg.cc/pLFHbFJn/EJ1-C3lm-XYAAmgr-D.jpg', 'https://i.postimg.cc/HsjmzKJz/72b54337-a2ce-4b50-82cf-0c8125c6e2ce.webp', 'https://i.postimg.cc/HsjmzKJz/72b54337-a2ce-4b50-82cf-0c8125c6e2ce.webp', '<iframe class="h-video" src="https://www.youtube.com/embed/9TtXI4jk22s?si=o98opwKpTh6SWJgU\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Steve Aoki', 'Miami, Florida, Estados Unidos', 'estadounidense', 'Steven Hiroyuki Aoki, más conocido como Steve Aoki, es un DJ, remezclador y productor discográfico estadounidense de origen japonés; también dueño y fundador del sello musical Dim Mak Records. En 2011, debutó en la lista Top 100 DJs de la revista DJ Mag, ingresando directamente al puesto #42. Tanto en 2016 como en 2022, se ubicó en el séptimo puesto, siendo esta su mejor posición en la lista.', 'https://i.postimg.cc/8k09pC5d/steve-aoki.jpg', 'https://i.postimg.cc/rwSPNC9g/Steve-Aoki-revela-su-rutina-de-longevidad-y-es-intensa-1024x642.jpg', 'https://i.postimg.cc/rwSPNC9g/Steve-Aoki-revela-su-rutina-de-longevidad-y-es-intensa-1024x642.jpg', '<iframe class="h-video" src="https://www.youtube.com/embed/_36t06naY1Y?si=zJNL3ChuAjXs8Ona\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Hernán Cattaneo', 'Buenos Aires, Argentina', 'argentino', 'Hernán Cattaneo es un DJ y productor argentino, que se dedica principalmente al Progressive House.​ En el año 2018, ganó el premio al mejor DJ en este género otorgado por DJ Awards de Ibiza.', 'https://i.postimg.cc/VvpVDKTZ/hernan-cattaneo.jpg', 'https://i.postimg.cc/0jTVpbML/Hernan-Cattaneo.png', 'https://i.postimg.cc/0jTVpbML/Hernan-Cattaneo.png', '<iframe class="h-video" src="https://www.youtube.com/embed/Easqg4SUl2Q?si=8J2b4EsnTV-ZINUg\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Martin Garrix', 'Amstelveen, Países Bajos', 'neerlandés', 'Martijn Gerard Garritsen,​ conocido artísticamente como Martin Garrix, es un DJ, remezclador y productor neerlandés de electro-house y Big Room House; dueño y fundador del sello discográfico STMPD RCRDS. También trabaja bajos los seudónimos Ytram y GRX. Actualmente ocupa el puesto #3 en la encuesta realizada en 2023 por la revista DJ Mag. En 2013, ingresó a la encuesta anual Top 100 DJs de DJ Mag, directamente al puesto #40. En 2014, obtuvo el cuarto puesto y en 2015 fue nombrado tercero. En 2016, 2017, 2018 y 2022 fue elegido por la revista como mejor DJ del mundo, colocándolo en el puesto número #1. En 2019 descendió al segundo puesto y en 2020 al tercero. Alcanzó el reconocimiento internacional gracias a su canción «Animals», lanzado el 17 de junio de 2013, bajo la discográfica Spinnin Records. La canción alcanzó el puesto #1 en Bélgica y en Reino Unido, y el puesto #3 en Irlanda. El sencillo «Wizard», producido con Jay Hardway, también fue un éxito en numerosos países durante 2013.', 'https://i.postimg.cc/kXRZBd60/martin-garrix.png', 'https://i.postimg.cc/FHrhcRyf/Martin-Garrix-Ankle.jpg', 'https://i.postimg.cc/FHrhcRyf/Martin-Garrix-Ankle.jpg', '<iframe class="h-video" src="https://www.youtube.com/embed/WKuaujIHBT4?si=XLgmb4CNve1mHr4f\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Peggy Gou', 'Incheon, Bandera de Corea del Sur Corea del Sur', 'surcoreana', 'Peggy Gou, de nombre real Kim Min-ji, es una DJ surcoreana, además de productora musical y diseñadora de moda. Ha lanzado siete EP en sellos discográficos que incluyen Ninja Tune y Phonica Records. En 2019, lanzó su propio sello discográfico, Gudu Records, que lleva la fusión de géneros a la pista de baile. Actualmente ocupa el puesto #9 en la encuesta realizada en 2023 por la revista DJ Mag.', 'https://i.postimg.cc/505k3gKY/peggy-avatar.webp', 'https://i.postimg.cc/5yxKkzDP/peggy2.webp', 'https://i.postimg.cc/XqQ1MJbn/peggy3.png', '<iframe class="h-video" src="https://www.youtube.com/embed/Zy1GyGDynGk?si=_PXNCm9NnHH1K5s8\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'),
('Charlotte de Witte', 'Gante, Bélgica', 'belga', 'Charlotte de Witte es una DJ y productora belga. Es conocida por sus sets de techno minimalista. Anteriormente utilizó el seudónimo de Raving George, debido a que la gente tenía prejuicios con las mujeres DJs.', 'https://i.postimg.cc/NfdSSNsR/charlotte-avatar.jpg', 'https://i.postimg.cc/gJ5bCNqM/charlotte2.jpg', 'https://i.postimg.cc/RhHx4Kgv/charlotte3.png', '<iframe class="h-video" src="https://www.youtube.com/embed/vNSm96XYgfA?si=pklngVoe0eIGjr9e\" title="YouTube video player\" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin"allowfullscreen></iframe>');
