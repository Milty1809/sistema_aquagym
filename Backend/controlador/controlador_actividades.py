from flask import Blueprint, render_template

from Backend.modelo.modelo_actividades import ModeloActividad

controlador_actividades = Blueprint(
    "controlador_actividades",
    __name__
)

@controlador_actividades.route(
    "/panel_cl/actividades"
)
def actividades():

    datos = ModeloActividad.obtener_actividades()

    return render_template(
        "interfaz_cliente/paneles_cl/actividades/index.html",
        actividades=datos
    )