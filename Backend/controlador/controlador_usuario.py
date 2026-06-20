from flask import Blueprint, flash, redirect, render_template, request

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
    
    if ModeloUsuario.existe_usuario(username):
        flash("El nombre de usuario ya existe")
        return redirect('/registro')

    ModeloUsuario.registrar_usuario(
        nombre,
        apellido,
        password,
        rol,
        username
    )

    flash("Usuario registrado exitosamente")

    return redirect('/registro')

@controlador_usuario.route(
    '/usuarios',
    methods=['GET', 'POST']
)
def usuarios():

    usuario_edit = None

    if request.method == 'POST':

        accion = request.form.get('accion')

        if accion == 'guardar':

            nombre = request.form['nombre']
            apellido = request.form['apellido']
            usuario = request.form['usuario']
            password = request.form['password']
            rol = request.form['rol']

            if ModeloUsuario.existe_usuario(usuario):

                flash(
                    "El usuario ya existe"
                )

            else:

                ModeloUsuario.registrar_usuario(
                    nombre,
                    apellido,
                    password,
                    rol,
                    usuario
                )

                flash(
                    "Usuario registrado correctamente"
                )

        elif accion == 'editar':

            ModeloUsuario.editar_usuario(
                request.form['id_usuario'],
                request.form['nombre'],
                request.form['apellido'],
                request.form['password'],
                request.form['rol'],
                request.form['usuario']
            )

            flash(
                "Usuario actualizado correctamente"
            )

        elif accion == 'eliminar':

            ModeloUsuario.eliminar_usuario(
                request.form['id_usuario']
            )

            flash(
                "Usuario eliminado correctamente"
            )

        elif accion == 'seleccionar':

            usuario_edit = {
                'id_usuario': request.form['id_usuario'],
                'nombre': request.form['nombre'],
                'apellido': request.form['apellido'],
                'usuario': request.form['usuario'],
                'password': request.form['password'],
                'rol': request.form['rol']
            }

    usuarios = ModeloUsuario.obtener_usuarios()

    return render_template(
        'interfaz_admin/paneles_ad/reg_usuarios/index.html',
        usuarios=usuarios,
        usuario_edit=usuario_edit
    )