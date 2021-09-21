from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/rockoladb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos
from models import Song

# Crear el esquema de la DB
db.create_all()
db.session.commit()

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

        # insertar canción
        name = "Imagine"
        artist = "John Lennon"
        genre = "Rock"
        album = "Imagine"
        year = 1971
        link = "https://www.youtube.com/watch?v=YkgkThdzX-8"

        entry = Song(name,artist,genre,album,year,link)
        db.session.add(entry)
        db.session.commit()

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