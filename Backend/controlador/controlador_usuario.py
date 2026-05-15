from flask import Blueprint, flash, redirect, request

from Backend.modelo.modelo_usuario import ModeloUsuario

controlador_usuario = Blueprint('controlador_usuario', __name__)


@controlador_usuario.route('/registrar', methods=['POST'])
def registrar():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    username = request.form['username']
    rol = "cliente"

    password = request.form['password']
    confirmar_password = request.form['confirmar_password']

    if nombre == "" or apellido == "" or username == "" or password == "" or confirmar_password == "":
        flash("Todos los campos son obligatorios")
        return redirect('/registro')

    if password != confirmar_password:
        flash("Las contraseñas no coinciden")
        return redirect('/registro')

    usuarios_existentes = ["admin", "fabricio", "juan"]

    if username in usuarios_existentes:
        flash("El nombre de usuario ya existe")
        return redirect('/registro')

    ModeloUsuario.registrar_usuario(
        nombre,
        apellido,
        username,
        rol,
        password
    )

    flash("Usuario registrado exitosamente")

    return redirect('/registro')