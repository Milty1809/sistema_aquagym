import os
from flask import Flask, flash, redirect, request, render_template, send_from_directory
from dotenv import load_dotenv

from Backend.modelo.modelo_usuario import ModeloUsuario

load_dotenv()

app = Flask(
    __name__,
    template_folder='../../Frontend/interfaz_registro_usu_cl',
    static_folder='../../Frontend/interfaz_registro_usu_cl'
)
app.secret_key = "123"

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/login')
def login():
    return send_from_directory(
        '../Frontend/interfaz_inicio_sesion',
        'index.html'
    )


@app.route('/registrar', methods=['POST'])
def registrar():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    username = request.form['username']
    rol = "cliente"
    password = request.form['password']
    confirmar_password = request.form['confirmar_password']
    
    # VALIDAR CAMPOS VACÍOS
    if nombre == "" or apellido == "" or username == "" or password == "" or confirmar_password == "":
        flash("Todos los campos son obligatorios")
        return redirect("/")

    # VALIDAR CONTRASEÑAS
    if password != confirmar_password:
        flash("Las contraseñas no coinciden")
        return redirect("/")

    # VALIDAR USUARIO REPETIDO
    usuarios_existentes = ["admin", "fabricio", "juan"]

    if username in usuarios_existentes:
        flash("El nombre de usuario ya existe")
        return redirect("/")

    ModeloUsuario.registrar_usuario(
    nombre,
    apellido,
    username,
    rol,
    password
)

    flash("Usuario registrado exitosamente")
    return redirect("/")


app.run(debug=True)