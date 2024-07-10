# Importaciones
from flask import Flask
from flask import request, jsonify, make_response, render_template
from flask_mysqldb import MySQL
# from flask_cors import CORS, cross_origin

# Configuración de aplicación y base de datos
app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "https://amil.netlify.app/"}})
mysql = MySQL(app)
app.config['MYSQLHOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_PORT']= 3307
app.config['MYSQL_DB']= 'amil'

# Rutas

# Rutas de vistas
@app.route('/')
def generar_vista_index():
    try:
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
            """
        
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(sql)
        
        events = cursor.fetchall()
        
        print("-"*60)
        for evento in events:
            print(evento)
            print("-"*60)
        
        cursor.close()
        
        if events:
            return render_template('index.html', eventos=events)
        else:
            return make_response(jsonify({'error': 'No se encontraron eventos'}), 404)
    except Exception as e:
        print(f"Error: {e}")
        return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# Rutas de géneros
# @app.route('/api/generos', methods=['POST'])
# def create_genero():
    
#     data = request.get_json()
#     _genero = data.get('genero')
#     _descripcion = data.get('descripcion')
    
#     datos = (_genero, _descripcion)
    
#     sql = "INSERT INTO `generos`(`id`, `genero`, `descripcion`) VALUES (NULL,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_genero = {
#         'id': new_id,
#         'genero': _genero,
#         'descripcion': _descripcion
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_genero), 201)

# @app.route('/api/generos')
# def read_genero():
    
#     sql = "SELECT * FROM generos"
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql)
    
#     db_generos = cursor.fetchall()
    
#     generos = []
#     for genero in db_generos:
#         generos.append({
#             'id': genero[0],
#             'genero': genero[1],
#             'descripcion': genero[2],
#         })
        
#     cursor.close()
#     return make_response(jsonify(generos), 200)

# @app.route('/api/generos/<int:id>', methods=['POST'])
# def update_genero_by_id(id):
    
#     sql = "SELECT * FROM generos WHERE id = %s"
    
#     data = request.get_json()
#     _genero = data.get('genero')
#     _descripcion = data.get('descripcion')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _genero is not None:
#         update_fields.append("genero=%s")
#         params.append(_genero)
        
#     if _descripcion is not None:
#         update_fields.append("descripcion=%s")
#         params.append(_descripcion)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.generos SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT genero, descripcion FROM amil.generos WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             "id": id,
#             "genero": updated_row[0],
#             "descripcion": updated_row[1]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/generos/<int:id>', methods=['DELETE'])
# def destroy_genero_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`generos` WHERE id=%s", (id,))
#     genero = cursor.fetchone()
    
#     if genero:
#         cursor.execute("DELETE FROM `amil`.`generos` WHERE id=%s", (id,))
#         conn.commit()
#         genero_dict = {
#             'id': genero[0],
#             'genero': genero[1],
#             'descripcion': genero[2]
#         }
        
#         cursor.close()
#         return make_response(jsonify(genero_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Género no encontrado'}), 404)

# # Rutas de lugares
# @app.route('/api/lugares', methods=['POST'])
# def create_lugar():
    
#     data = request.get_json()
#     _lugar = data.get('lugar')
#     _direccion = data.get('direccion')
#     _ciudad = data.get('ciudad')
    
#     datos = (_lugar, _direccion, _ciudad)
    
#     sql = "INSERT INTO `lugares`(`id`, `lugar`, `direccion`, `ciudad`) VALUES (NULL,%s,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_lugar = {
#         'id': new_id,
#         'lugar': _lugar,
#         'direccion': _direccion,
#         'ciudad': _ciudad
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_lugar), 201)

# @app.route('/api/lugares/<int:id>')
# def read_lugar_by_id(id):
    
#     sql = "SELECT * FROM lugares WHERE id = %s"
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, (id,))
    
#     lugar = cursor.fetchone()
    
#     if lugar:
#         lugar_dict = {
#             'id': lugar[0],
#             'lugar': lugar[1],
#             'direccion': lugar[2],
#             'ciudad': lugar[3],
#         }
#         cursor.close()
#         return make_response(jsonify(lugar_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Lugar no encontrado'}), 404)
    
# @app.route('/api/lugares/<int:id>', methods=['POST'])
# def update_lugar_by_id(id):
    
#     sql = "SELECT * FROM lugares WHERE id = %s"
    
#     data = request.get_json()
#     _lugar = data.get('lugar')
#     _direccion = data.get('direccion')
#     _ciudad = data.get('ciudad')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _lugar is not None:
#         update_fields.append("lugar=%s")
#         params.append(_lugar)
        
#     if _direccion is not None:
#         update_fields.append("direccion=%s")
#         params.append(_direccion)
        
#     if _ciudad is not None:
#         update_fields.append("ciudad=%s")
#         params.append(_ciudad)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.lugares SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT lugar, direccion, ciudad FROM amil.lugares WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             "id": id,
#             "lugar": updated_row[0],
#             "direccion": updated_row[1],
#             "ciudad": updated_row[2]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/lugares/<int:id>', methods=['DELETE'])
# def destroy_lugar_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`lugares` WHERE id=%s", (id,))
#     lugar = cursor.fetchone()
    
#     if lugar:
#         cursor.execute("DELETE FROM `amil`.`lugares` WHERE id=%s", (id,))
#         conn.commit()
#         lugar_dict = {
#             'id': lugar[0],
#             "lugar": lugar[0],
#             "direccion": lugar[1],
#             "ciudad": lugar[2]
#         }
        
#         cursor.close()
#         return make_response(jsonify(lugar_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Lugar no encontrado'}), 404)

# # Rutas de artistas
# @app.route('/api/artistas', methods=['POST'])
# def create_artista():
    
#     data = request.get_json()
#     _artista = data.get('artista')
#     _imagen = data.get('imagen')
#     _avatar = data.get('avatar')
#     _foto = data.get('foto')
#     _video = data.get('video')
#     _origen = data.get('origen')
#     _nacionalidad = data.get('nacionalidad')
#     _descripcion = data.get('descripcion')
#     _genero_id = data.get('genero_id')
    
#     datos = (_artista, _imagen, _avatar, _foto, _video, _origen, _nacionalidad, _descripcion, _genero_id)
    
#     sql = "INSERT INTO `artistas`(`id`, `artista`, `imagen`, `avatar`, `foto`, `video`, `origen`, `nacionalidad`, `descripcion`, `genero_id`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_artista = {
#         'id': new_id,
#         'artista': _artista,
#         'imagen': _imagen,
#         'avatar': _avatar,
#         'foto': _foto,
#         'video': _video,
#         'origen': _origen,
#         'nacionalidad': _nacionalidad,
#         'descripcion': _descripcion,
#         'genero_id': _genero_id
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_artista), 201)

# @app.route('/api/artistas/<int:id>')
# def read_artista_by_id(id):
    
#     sql = "SELECT * FROM artistas WHERE id = %s"
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, (id,))
    
#     artista = cursor.fetchone()
    
#     if artista:
#         artista_dict = {
#             'id': artista[0],
#             'artista': artista[1],
#             'imagen': artista[2],
#             'avatar': artista[3],
#             'foto': artista[4],
#             'video': artista[5],
#             'origen': artista[6],
#             'nacionalidad': artista[7],
#             'descripcion': artista[8],
#             'genero_id': artista[9]
#         }
#         cursor.close()
#         return make_response(jsonify(artista_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Artista no encontrado'}), 404)
    
# @app.route('/api/artistas/<int:id>', methods=['POST'])
# def update_artista_by_id(id):
    
#     data = request.get_json()
#     _artista = data.get('artista')
#     _imagen = data.get('imagen')
#     _avatar = data.get('avatar')
#     _foto = data.get('foto')
#     _video = data.get('video')
#     _origen = data.get('origen')
#     _nacionalidad = data.get('nacionalidad')
#     _descripcion = data.get('descripcion')
#     _genero_id = data.get('genero_id')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _artista is not None:
#         update_fields.append("artista=%s")
#         params.append(_artista)
        
#     if _imagen is not None:
#         update_fields.append("imagen=%s")
#         params.append(_imagen)
        
#     if _avatar is not None:
#         update_fields.append("avatar=%s")
#         params.append(_avatar)
        
#     if _foto is not None:
#         update_fields.append("foto=%s")
#         params.append(_foto)
        
#     if _video is not None:
#         update_fields.append("video=%s")
#         params.append(_video)
    
#     if _origen is not None:
#         update_fields.append("origen=%s")
#         params.append(_origen)
        
#     if _nacionalidad is not None:
#         update_fields.append("nacionalidad=%s")
#         params.append(_nacionalidad)
    
#     if _descripcion is not None:
#         update_fields.append("descripcion=%s")
#         params.append(_descripcion)
        
#     if _genero_id is not None:
#         update_fields.append("genero_id=%s")
#         params.append(_genero_id)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.artistas SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT id, artista, imagen, avatar, foto, video, origen, nacionalidad, descripcion, genero_id FROM amil.artistas WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             'id': updated_row[0],
#             'artista': updated_row[1],
#             'imagen': updated_row[2],
#             'avatar': updated_row[3],
#             'foto': updated_row[4],
#             'video': updated_row[5],
#             'origen': updated_row[6],
#             'nacionalidad': updated_row[7],
#             'descripcion': updated_row[8],
#             'genero_id': updated_row[9]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/artistas/<int:id>', methods=['DELETE'])
# def destroy_artista_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`artistas` WHERE id=%s", (id,))
#     artista = cursor.fetchone()
    
#     if artista:
#         cursor.execute("DELETE FROM `amil`.`artistas` WHERE id=%s", (id,))
#         conn.commit()
#         artista_dict = {
#             'id': artista[0],
#             'artista': artista[1],
#             'imagen': artista[2],
#             'avatar': artista[3],
#             'foto': artista[4],
#             'video': artista[5],
#             'origen': artista[6],
#             'nacionalidad': artista[7],
#             'descripcion': artista[8],
#             'genero_id': artista[9]
#         }
        
#         cursor.close()
#         return make_response(jsonify(artista_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Artista no encontrado'}), 404)

# # Rutas de entradas
# @app.route('/api/entradas', methods=['POST'])
# def create_entrada():
    
#     data = request.get_json()
#     _tipo = data.get('tipo')
#     _precio = data.get('precio')
#     _cantidad = data.get('cantidad')
    
#     datos = (_tipo, _precio, _cantidad)
    
#     sql = "INSERT INTO `entradas`(`id`, `tipo`, `precio`, `cantidad`) VALUES (NULL,%s,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_entrada = {
#         'id': new_id,
#         'tipo': _tipo,
#         'precio': _precio,
#         'cantidad': _cantidad
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_entrada), 201)

# @app.route('/api/entradas')
# def read_entrada():
    
#     sql = "SELECT * FROM entradas"
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql)
    
#     db_entradas = cursor.fetchall()
    
#     entradas = []
#     for entrada in db_entradas:
#         entradas.append({
#             'id': entrada[0],
#             'tipo': entrada[1],
#             'precio': entrada[2],
#             'cantidad': entrada[3]
#         })
        
#     cursor.close()
#     return make_response(jsonify(entradas), 200)

# @app.route('/api/entradas/<int:id>', methods=['POST'])
# def update_entrada_by_id(id):
    
#     data = request.get_json()
#     _tipo = data.get('tipo')
#     _precio = data.get('precio')
#     _cantidad = data.get('cantidad')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _tipo is not None:
#         update_fields.append("tipo=%s")
#         params.append(_tipo)
        
#     if _precio is not None:
#         update_fields.append("precio=%s")
#         params.append(_precio)
        
#     if _cantidad is not None:
#         update_fields.append("cantidad=%s")
#         params.append(_cantidad)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.entradas SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT id, tipo, precio, cantidad FROM amil.entradas WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             'id': updated_row[0],
#             'tipo': updated_row[1],
#             'precio': updated_row[2],
#             'cantidad': updated_row[3]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/entradas/<int:id>', methods=['DELETE'])
# def destroy_entrada_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`entradas` WHERE id=%s", (id,))
#     entrada = cursor.fetchone()
    
#     if entrada:
#         cursor.execute("DELETE FROM `amil`.`entradas` WHERE id=%s", (id,))
#         conn.commit()
#         entrada_dict = {
#             'id': entrada[0],
#             'tipo': entrada[1],
#             'precio': entrada[2],
#             'cantidad': entrada[3]
#         }
        
#         cursor.close()
#         return make_response(jsonify(entrada_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Entrada no encontrada'}), 404)

# # Rutas de horarios
# @app.route('/api/horarios', methods=['POST'])
# def create_horario():
    
#     data = request.get_json()
#     _desde = data.get('desde')
#     _hasta = data.get('hasta')
#     _artista_id = data.get('artista_id')
    
#     datos = (_desde, _hasta, _artista_id)
    
#     sql = "INSERT INTO `horarios`(`id`, `desde`, `hasta`, `artista_id`) VALUES (NULL,%s,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_horario = {
#         'id': new_id,
#         'desde': _desde,
#         'hasta': _hasta,
#         'artista_id': _artista_id
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_horario), 201)

# @app.route('/api/horarios')
# def read_horario():
    
#     sql = "SELECT * FROM horarios"
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql)
    
#     db_horarios = cursor.fetchall()
    
#     horarios = []
#     for horario in db_horarios:
#         horarios.append({
#             'id': horario[0],
#             'desde': horario[1],
#             'hasta': horario[2],
#             'artista_id': horario[3]
#         })
        
#     cursor.close()
#     return make_response(jsonify(horarios), 200)

# @app.route('/api/horarios/<int:id>', methods=['POST'])
# def update_horario_by_id(id):
    
#     data = request.get_json()
#     _desde = data.get('desde')
#     _hasta = data.get('hasta')
#     _artista_id = data.get('artista_id')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _desde is not None:
#         update_fields.append("desde=%s")
#         params.append(_desde)
        
#     if _hasta is not None:
#         update_fields.append("hasta=%s")
#         params.append(_hasta)
        
#     if _artista_id is not None:
#         update_fields.append("artista_id=%s")
#         params.append(_artista_id)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.horarios SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT id, desde, hasta, artista_id FROM amil.horarios WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             'id': updated_row[0],
#             'desde': updated_row[1],
#             'hasta': updated_row[2],
#             'artista_id': updated_row[3]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/horarios/<int:id>', methods=['DELETE'])
# def destroy_horario_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`horarios` WHERE id=%s", (id,))
#     horario = cursor.fetchone()
    
#     if horario:
#         cursor.execute("DELETE FROM `amil`.`horarios` WHERE id=%s", (id,))
#         conn.commit()
#         horario_dict = {
#             'id': horario[0],
#             'desde': horario[1],
#             'hasta': horario[2],
#             'artista_id': horario[3]
#         }
        
#         cursor.close()
#         return make_response(jsonify(horario_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Horario no encontrado'}), 404)

# # Rutas de eventos
# @app.route('/api/eventos', methods=['POST'])
# def create_evento():
    
#     data = request.get_json()
#     _dia = data.get('dia')
#     _mes = data.get('mes')
#     _anio = data.get('anio')
#     _inicio = data.get('inicio')
#     _cierre = data.get('cierre')
#     _lugar_id = data.get('lugar_id')
#     _artista_id = data.get('artista_id')
#     _entrada_id = data.get('entrada_id')
#     _horario_id = data.get('horario_id')
    
#     datos = (_dia, _mes, _anio, _inicio, _cierre, _lugar_id, _artista_id, _entrada_id, _horario_id)
    
#     sql = "INSERT INTO `eventos`(`id`, `dia`, `mes`, `anio`, `inicio`, `cierre`, `lugar_id`, `artista_id`, `entrada_id`, `horario_id`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, datos)
#     conn.commit()
    
#     new_id = cursor.lastrowid
    
#     created_evento = {
#         'id': new_id,
#         'dia': _dia,
#         'mes': _mes,
#         'anio': _anio,
#         'inicio': _inicio,
#         'cierre': _cierre,
#         'lugar_id': _lugar_id,
#         'artista_id': _artista_id,
#         'entrada_id': _entrada_id,
#         'horario_id': _horario_id
#     }
    
#     cursor.close()
    
#     return make_response(jsonify(created_evento), 201)

# # @cross_origin(origin='https://amil.netlify.app')
# @app.route('/api/eventos')
# def read_eventos():
#     try:
#         sql = """
#                 SELECT 
#                     eventos.id, eventos.dia, eventos.mes, eventos.anio, eventos.inicio, eventos.cierre, 
#                     lugares.lugar, lugares.ciudad, lugares.direccion,
#                     artistas.artista, artistas.avatar, artistas.foto, artistas.imagen, artistas.video, artistas.descripcion,
#                     entradas.tipo, entradas.precio, entradas.cantidad,
#                     horarios.desde, horarios.hasta, horarios.artista_id
#                 FROM eventos
#                 INNER JOIN lugares ON eventos.lugar_id = lugares.id
#                 INNER JOIN artistas ON eventos.artista_id = artistas.id
#                 INNER JOIN entradas ON eventos.entrada_id = entradas.id
#                 INNER JOIN horarios ON eventos.horario_id = horarios.id
#             """
        
#         conn = mysql.connection
#         cursor = conn.cursor()
#         cursor.execute(sql)
        
#         eventos = cursor.fetchall()
        
#         eventos_list = []
#         for evento in eventos:
#             evento_dict = {
#                 'id': evento[0],
#                 'dia': evento[1],
#                 'mes': evento[2],
#                 'anio': evento[3],
#                 'inicio': evento[4],
#                 'cierre': evento[5],
#                 'lugar': {
#                         'nombre': evento[6],
#                         'ciudad': evento[7],
#                         'direccion': evento[8]
#                     },
#                 'artista': {
#                         'nombre': evento[9],
#                         'avatar': evento[10],
#                         'foto': evento[11],
#                         'imagen': evento[12],
#                         'video': evento[13],
#                         'descripcion': evento[14]
#                     },
#                 'entrada': {
#                         'tipo': evento[15],
#                         'precio': evento[16],
#                         'cantidad': evento[17]
#                     },
#                 'horario': {
#                         'desde': evento[18],
#                         'hasta': evento[19],
#                         'artista_id': evento[20]
#                 }
#             }
#             eventos_list.append(evento_dict)
        
#         cursor.close()
        
#         if eventos_list:
#             return make_response(jsonify(eventos_list), 200)
#         else:
#             return make_response(jsonify({'error': 'No se encontraron eventos'}), 404)
#     except Exception as e:
#         print(f"Error: {e}")
#         return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# @app.route('/api/eventos/<int:id>')
# def read_evento_by_id(id):
    
#     sql = """
#             SELECT 
#                 eventos.id, eventos.dia, eventos.mes, eventos.anio, eventos.inicio, eventos.cierre, 
#                 lugares.lugar, lugares.ciudad, lugares.direccion,
#                 artistas.artista, artistas.avatar, artistas.foto, artistas.imagen, artistas.video, artistas.descripcion,
#                 entradas.tipo, entradas.precio, entradas.cantidad,
#                 horarios.desde, horarios.hasta, horarios.artista_id
#             FROM eventos
#             INNER JOIN lugares ON eventos.lugar_id = lugares.id
#             INNER JOIN artistas ON eventos.artista_id = artistas.id
#             INNER JOIN entradas ON eventos.entrada_id = entradas.id
#             INNER JOIN horarios ON eventos.horario_id = horarios.id
#             WHERE eventos.id = %s
#         """
    
#     conn = mysql.connection
#     cursor = conn.cursor()
#     cursor.execute(sql, (id,))
    
#     evento = cursor.fetchone()
    
#     if evento:
#         evento_dict = {
#             'id': evento[0],
#             'dia': evento[1],
#             'mes': evento[2],
#             'anio': evento[3],
#             'inicio': evento[4],
#             'cierre': evento[5],
#             'lugar': {
#                     'nombre': evento[6],
#                     'ciudad': evento[7],
#                     'direccion': evento[8]
#                 },
#             'artista': {
#                     'nombre': evento[9],
#                     'avatar': evento[10],
#                     'foto': evento[11],
#                     'imagen': evento[12],
#                     'video': evento[13],
#                     'descripcion': evento[14]
#                 },
#             'entrada': {
#                     'tipo': evento[15],
#                     'precio': evento[16],
#                     'cantidad': evento[17]
#                 },
#             'horario': {
#                     'desde': evento[18],
#                     'hasta': evento[19],
#                     'artista_id': evento[20]
#             }
#         }
#         cursor.close()
#         return make_response(jsonify(evento_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Evento no encontrado'}), 404)
    
# @app.route('/api/eventos/<int:id>', methods=['POST'])
# def update_evento_by_id(id):
    
#     data = request.get_json()
#     _dia = data.get('dia')
#     _mes = data.get('mes')
#     _anio = data.get('anio')
#     _inicio = data.get('inicio')
#     _cierre = data.get('cierre')
#     _lugar_id = data.get('lugar_id')
#     _artista_id = data.get('artista_id')
#     _entrada_id = data.get('entrada_id')
#     _horario_id = data.get('horario_id')
    
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     update_fields = []
#     params = []
    
#     if _dia is not None:
#         update_fields.append("dia=%s")
#         params.append(_dia)
        
#     if _mes is not None:
#         update_fields.append("mes=%s")
#         params.append(_mes)
        
#     if _anio is not None:
#         update_fields.append("anio=%s")
#         params.append(_anio)
        
#     if _inicio is not None:
#         update_fields.append("inicio=%s")
#         params.append(_inicio)
        
#     if _cierre is not None:
#         update_fields.append("cierre=%s")
#         params.append(_cierre)
    
#     if _lugar_id is not None:
#         update_fields.append("lugar_id=%s")
#         params.append(_lugar_id)
        
#     if _artista_id is not None:
#         update_fields.append("artista_id=%s")
#         params.append(_artista_id)
    
#     if _entrada_id is not None:
#         update_fields.append("entrada_id=%s")
#         params.append(_entrada_id)
        
#     if _horario_id is not None:
#         update_fields.append("horario_id=%s")
#         params.append(_horario_id)
    
#     if not update_fields:
#         return make_response(jsonify({"error": "No hay campos para actualizar. Envíe los campos correctos."}), 400)
    
#     params.append(id)
#     sql = "UPDATE amil.eventos SET " + ", ".join(update_fields) + " WHERE id=%s"
#     cursor.execute(sql, params)
    
#     conn.commit()
    
#     cursor.execute("SELECT id, dia, mes, anio, inicio, cierre, lugar_id, artista_id, entrada_id, horario_id FROM amil.eventos WHERE id=%s", (id,))
#     updated_row = cursor.fetchone()
#     cursor.close()
    
#     if updated_row:
#         updated_object = {
#             'id': updated_row[0],
#             'dia': updated_row[1],
#             'mes': updated_row[2],
#             'anio': updated_row[3],
#             'inicio': updated_row[4],
#             'cierre': updated_row[5],
#             'lugar_id': updated_row[6],
#             'artista_id': updated_row[7],
#             'entrada_id': updated_row[8],
#             'horario_id': updated_row[9]
#         }
#         return make_response(jsonify(updated_object), 200)
#     else:
#         return make_response(jsonify({"error": "Registro no encontrado."}), 404)
    
# @app.route('/api/eventos/<int:id>', methods=['DELETE'])
# def destroy_evento_by_id(id):
#     conn = mysql.connection
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM `amil`.`eventos` WHERE id=%s", (id,))
#     evento = cursor.fetchone()
    
#     if evento:
#         cursor.execute("DELETE FROM `amil`.`eventos` WHERE id=%s", (id,))
#         conn.commit()
#         evento_dict = {
#             'id': evento[0],
#             'dia': evento[1],
#             'mes': evento[2],
#             'anio': evento[3],
#             'inicio': evento[4],
#             'cierre': evento[5],
#             'lugar_id': evento[6],
#             'artista_id': evento[7],
#             'entrada_id': evento[8],
#             'horario_id': evento[9]
#         }
        
#         cursor.close()
#         return make_response(jsonify(evento_dict), 200)
#     else:
#         cursor.close()
#         return make_response(jsonify({'error': 'Evento no encontrado'}), 404)

if __name__ == "__main__":
    app.run(debug=True)