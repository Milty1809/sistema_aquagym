from flask import Blueprint, render_template, request

from Backend.modelo.modelo_clientes import ModeloClientes

controlador_clientes = Blueprint(
    "controlador_clientes",
    __name__
)

# RECEPCIONISTA
@controlador_clientes.route(
    "/panel_rc/reg_clientes",
    methods=["GET", "POST"]
)
def clientes():

    cliente = None

    # POST
    if request.method == "POST":

        accion = request.form["accion"]

        # GUARDAR
        if accion == "guardar":

            nombre = request.form["nombre"]

            apellido = request.form["apellido"]

            ci = request.form["ci"]

            ModeloClientes.registrar_cliente(
                nombre,
                apellido,
                ci
            )

        # SELECCIONAR
        elif accion == "seleccionar":

            cliente = {

                "id_cliente":
                request.form["id_cliente"],

                "nombre":
                request.form["nombre"],

                "apellido":
                request.form["apellido"],

                "ci":
                request.form["ci"]

            }
        # EDITAR
        elif accion == "editar":

            id_cliente = request.form[
                "id_cliente"
            ]

            nombre = request.form[
                "nombre"
            ]

            apellido = request.form[
                "apellido"
            ]

            ci = request.form[
                "ci"
            ]

            ModeloClientes.editar_cliente(
                id_cliente,
                nombre,
                apellido,
                ci
            )

        # ELIMINAR
        elif accion == "eliminar":

            id_cliente = request.form[
                "id_cliente"
            ]

            ModeloClientes.eliminar_cliente(
                id_cliente
            )

    # OBTENER CLIENTES
    datos = ModeloClientes.obtener_clientes()

    # RETORNAR VISTA
    return render_template(
        "interfaz_recepcionista/paneles_rc/reg_cliente/index.html",

        clientes=datos,

        cliente=cliente
    )