# Importaciones
from flask import Flask
from flask import request, jsonify, make_response
from flask_mysqldb import MySQL

# Configuración de aplicación y base de datos
app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQLHOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= '1234'
app.config['MYSQL_PORT']= 3306
app.config['MYSQL_DB']= 'amil'

# Rutas
# Rutas de géneros
@app.route('/api/generos', methods=['POST'])
def create_genero():
    
    data = request.get_json()
    _genero = data.get('genero')
    _descripcion = data.get('descripcion')
    
    datos = (_genero, _descripcion)
    
    sql = "INSERT INTO `generos`(`id`, `genero`, `descripcion`) VALUES (NULL,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return make_response(jsonify(datos), 200)

@app.route('/api/generos')
def read_genero():
    
    sql = "SELECT * FROM generos"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_generos = cursor.fetchall()
    
    generos = []
    for genero in db_generos:
        generos.append({
            'id': genero[0],
            'genero': genero[1],
            'descripcion': genero[2],
        })
        
    cursor.close()
    return make_response(jsonify(generos), 200)

# Rutas de lugares
@app.route('/api/lugares', methods=['POST'])
def create_lugar():
    
    data = request.get_json()
    _lugar = data.get('lugar')
    _direccion = data.get('direccion')
    _ciudad = data.get('ciudad')
    
    datos = (_lugar, _direccion, _ciudad)
    
    sql = "INSERT INTO `lugares`(`id`, `lugar`, `direccion`, `ciudad`) VALUES (NULL,%s,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return "<h1>Lugar creado</h1>"

@app.route('/api/lugares/<int:id>')
def read_lugar_by_id(id):
    
    sql = "SELECT * FROM lugares WHERE id = %s"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    
    lugar = cursor.fetchone()
    
    if lugar:
        lugar_dict = {
            'id': lugar[0],
            'lugar': lugar[1],
            'direccion': lugar[2],
            'ciudad': lugar[3],
        }
        cursor.close()
        return make_response(jsonify(lugar_dict), 200)
    else:
        cursor.close()
        return make_response(jsonify({'error': 'Lugar no encontrado'}), 404)

# Rutas de artistas
@app.route('/api/artistas', methods=['POST'])
def create_artista():
    
    data = request.get_json()
    _artista = data.get('artista')
    _imagen = data.get('imagen')
    _avatar = data.get('avatar')
    _foto = data.get('foto')
    _video = data.get('video')
    _origen = data.get('origen')
    _nacionalidad = data.get('nacionalidad')
    _descripcion = data.get('descripcion')
    _genero_id = data.get('genero_id')
    
    datos = (_artista, _imagen, _avatar, _foto, _video, _origen, _nacionalidad, _descripcion, _genero_id)
    
    sql = "INSERT INTO `artistas`(`id`, `artista`, `imagen`, `avatar`, `foto`, `video`, `origen`, `nacionalidad`, `descripcion`, `genero_id`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return "<h1>Artista creado</h1>"

@app.route('/api/artistas/<int:id>')
def read_artista_by_id(id):
    
    sql = "SELECT * FROM artistas WHERE id = %s"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    
    artista = cursor.fetchone()
    
    if artista:
        artista_dict = {
            'id': artista[0],
            'artista': artista[1],
            'imagen': artista[2],
            'avatar': artista[3],
            'foto': artista[4],
            'video': artista[5],
            'origen': artista[6],
            'nacionalidad': artista[7],
            'descripcion': artista[8],
            'genero_id': artista[9]
        }
        cursor.close()
        return make_response(jsonify(artista_dict), 200)
    else:
        cursor.close()
        return make_response(jsonify({'error': 'Artista no encontrado'}), 404)

# Rutas de entradas
@app.route('/api/entradas', methods=['POST'])
def create_entrada():
    
    data = request.get_json()
    _tipo = data.get('tipo')
    _precio = data.get('precio')
    _cantidad = data.get('cantidad')
    
    datos = (_tipo, _precio, _cantidad)
    
    sql = "INSERT INTO `entradas`(`id`, `tipo`, `precio`, `cantidad`) VALUES (NULL,%s,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return "<h1>Entrada creada</h1>"

@app.route('/api/entradas')
def read_entrada():
    
    sql = "SELECT * FROM entradas"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_entradas = cursor.fetchall()
    
    entradas = []
    for entrada in db_entradas:
        entradas.append({
            'id': entrada[0],
            'tipo': entrada[1],
            'precio': entrada[2],
            'cantidad': entrada[3]
        })
        
    cursor.close()
    return make_response(jsonify(entradas), 200)

# Rutas de horarios
@app.route('/api/horarios', methods=['POST'])
def create_horario():
    
    data = request.get_json()
    _desde = data.get('desde')
    _hasta = data.get('hasta')
    _artista_id = data.get('artista_id')
    
    datos = (_desde, _hasta, _artista_id)
    
    sql = "INSERT INTO `horarios`(`id`, `desde`, `hasta`, `artista_id`) VALUES (NULL,%s,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return "<h1>Horario creado</h1>"

@app.route('/api/horarios')
def read_horario():
    
    sql = "SELECT * FROM horarios"
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql)
    
    db_horarios = cursor.fetchall()
    
    horarios = []
    for horario in db_horarios:
        horarios.append({
            'id': horario[0],
            'desde': horario[1],
            'hasta': horario[2],
            'artista_id': horario[3]
        })
        
    cursor.close()
    return make_response(jsonify(horarios), 200)

# Rutas de eventos
@app.route('/api/eventos', methods=['POST'])
def create_evento():
    
    data = request.get_json()
    _dia = data.get('dia')
    _mes = data.get('mes')
    _anio = data.get('anio')
    _inicio = data.get('inicio')
    _cierre = data.get('cierre')
    _lugar_id = data.get('lugar_id')
    _artista_id = data.get('artista_id')
    _entrada_id = data.get('entrada_id')
    _horario_id = data.get('horario_id')
    
    datos = (_dia, _mes, _anio, _inicio, _cierre, _lugar_id, _artista_id, _entrada_id, _horario_id)
    
    sql = "INSERT INTO `eventos`(`id`, `dia`, `mes`, `anio`, `inicio`, `cierre`, `lugar_id`, `artista_id`, `entrada_id`, `horario_id`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return "<h1>Evento creado</h1>"

@app.route('/api/eventos/<int:id>')
def read_evento_by_id(id):
    
    sql = """
            SELECT 
                eventos.id, eventos.dia, eventos.mes, eventos.anio, eventos.inicio, eventos.cierre, 
                lugares.lugar, lugares.ciudad, lugares.direccion,
                artistas.artista, artistas.avatar, artistas.foto, artistas.imagen, artistas.video, artistas.descripcion,
                entradas.tipo, entradas.precio, entradas.cantidad,
                horarios.desde, horarios.hasta, horarios.artista_id
            FROM eventos
            INNER JOIN lugares ON eventos.lugar_id = lugares.id
            INNER JOIN artistas ON eventos.artista_id = artistas.id
            INNER JOIN entradas ON eventos.entrada_id = entradas.id
            INNER JOIN horarios ON eventos.horario_id = horarios.id
            WHERE eventos.id = %s
        """
    
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    
    evento = cursor.fetchone()
    
    if evento:
        evento_dict = {
            'id': evento[0],
            'dia': evento[1],
            'mes': evento[2],
            'anio': evento[3],
            'inicio': evento[4],
            'cierre': evento[5],
            'lugar': {
                    'nombre': evento[6],
                    'ciudad': evento[7],
                    'direccion': evento[8]
                },
            'artista': {
                    'nombre': evento[9],
                    'avatar': evento[10],
                    'foto': evento[11],
                    'imagen': evento[12],
                    'video': evento[13],
                    'descripcion': evento[14]
                },
            'entrada': {
                    'tipo': evento[15],
                    'precio': evento[16],
                    'cantidad': evento[17]
                },
            'horario': {
                    'desde': evento[18],
                    'hasta': evento[19],
                    'artista_id': evento[20]
            }
        }
        cursor.close()
        return make_response(jsonify(evento_dict), 200)
    else:
        cursor.close()
        return make_response(jsonify({'error': 'Evento no encontrado'}), 404)

if __name__ == "__main__":
    app.run(debug=True)