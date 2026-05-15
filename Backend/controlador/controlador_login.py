from flask import Blueprint, render_template, request, redirect, flash

controlador_login = Blueprint('controlador_login', __name__)


@controlador_login.route('/')
@controlador_login.route('/login')
def login():
    return render_template('interfaz_inicio_sesion/index.html')


@controlador_login.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():

    username = request.form['username']
    password = request.form['password']

    if username == "" or password == "":
        flash("Todos los campos son obligatorios")
        return redirect('/login')

    if username == "admin" and password == "1234":
        return "Inicio de sesión exitoso"

    flash("Usuario o contraseña incorrectos")
    return redirect('/login')


@controlador_login.route('/registro')
def registro():
    return render_template('interfaz_registro_usu_cl/index.html')