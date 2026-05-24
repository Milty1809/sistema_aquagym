from flask import Blueprint, render_template

from Backend.modelo.modelo_membresia import ModeloMembresia

controlador_membresia = Blueprint(
    "controlador_membresia",
    __name__
)

@controlador_membresia.route(
    "/panel_cl/membresias"
)
def membresias():

    # OBTENER DATOS MYSQL
    datos = ModeloMembresia.obtener_membresias()

    # ENVIAR AL HTML
    return render_template(
        "interfaz_cliente/paneles_cl/membresias/index.html",
        membresias=datos
    )