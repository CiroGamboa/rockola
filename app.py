from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/rockoladb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cnigyvvlnekmfd:cf8b7dd3929a83931b73ebe1c3b9577529801c18362d6fc2dbcea29e6ebadaed@ec2-54-161-189-150.compute-1.amazonaws.com:5432/d4po6l1jc02vka'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'some-secret-key' 

db = SQLAlchemy(app)

# Importar los modelos
from models import Song, User, Room

# Crear el esquema de la DB
db.create_all()
db.session.commit()

# Rutas de paginas
@app.route('/')
def home():
    return "This works"

@app.route('/example')
def example():
    return render_template("example.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/create-user', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]

    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    return "ok"


@app.route('/room')
def enter_room():
    return render_template("room.html")

@app.route('/create-room', methods=['POST'])
def create_room():
    room_code = request.form["room_code"]
    print("El codigo de sala es")
    print(room_code)

    return "ok"

if __name__ == "__main__":
    app.run()


    




























'''
@app.route('/post-request', methods=['POST'])
def post_req():
    request_data = request.form
    print(request_data)
    print(request_data['name'])

    return "Post success"

'''