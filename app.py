from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Rutas de paginas
@app.route('/')
def get_home():
    return 'Este es el home'

@app.route('/signup')
def sign_up():
    return 'Esta es la pagina de registro'

@app.route('/room')
def enter_room():
    return 'Esta es la pagina de una sala'


# Rutas de otras acciones
@app.route('/song', methods=['GET','POST'])
def crud_song():
    if request.method == 'GET':
        # Hago algo
        print("Llegó un GET")
        return 'Esto fue un GET'

    elif request.method == 'POST':
        # Registrar una cancion
        request_data = request.form
        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre:" + name)
        print("Artista:" + artist)
        print("Genero:" + genre)

        # Insertar en la base de datos la canción

        return 'Se registro la canción exitosamente'




    




























'''
@app.route('/post-request', methods=['POST'])
def post_req():
    request_data = request.form
    print(request_data)
    print(request_data['name'])

    return "Post success"

'''