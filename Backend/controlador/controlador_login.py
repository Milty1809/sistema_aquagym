from flask import Blueprint, render_template, request, redirect, flash
from Backend.modelo.modelo_login import ModeloLogin

controlador_login = Blueprint('controlador_login', __name__)


@controlador_login.route('/')
@controlador_login.route('/login')
def login():
    return render_template('interfaz_inicio_sesion/index.html')

@controlador_login.route('/interfazCL')
def interfazCL():
    return render_template('interfaz_cliente/index.html')

@controlador_login.route('/interfazAD')
def interfazAD():
    return render_template('interfaz_admin/index.html')

@controlador_login.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():

    username = request.form['username']
    password = request.form['password']

    if username == "" or password == "":
        flash("Todos los campos son obligatorios")
        return redirect('/login')

    usuario = ModeloLogin.iniciar_sesion(
        username,
        password
    )

    if usuario and usuario['rol'] == 'admin':

        flash("Inicio de sesión exitoso")

        return redirect('/interfazAD')
    
    if usuario and usuario['rol'] == 'cliente':

        flash("Inicio de sesión exitoso")

        return redirect('/interfazCL')

    flash("Usuario o contraseña incorrectos")

    return redirect('/login')


@controlador_login.route('/registro')
def registro():
    return render_template('interfaz_registro_usu_cl/index.html')