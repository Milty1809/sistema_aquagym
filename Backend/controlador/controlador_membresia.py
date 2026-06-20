from flask import Blueprint, render_template
from flask import request
from Backend.modelo.modelo_membresia import ModeloMembresia
from Backend.modelo.modelo_actividades import ModeloActividad
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

@controlador_membresia.route(
    "/panel_ad/reg_membresia",
    methods=["GET", "POST"]
)
def crud_membresias():

    membresia_edit = None

    if request.method == "POST":

        accion = request.form.get("accion")

        if accion == "guardar":

            ModeloMembresia.registrar_membresia(
                request.form["nombre"],
                request.form["duracion_dias"],
                request.form["precio"],
                request.form["id_actividad"]
            )

        elif accion == "editar":

            ModeloMembresia.editar_membresia(
                request.form["id_membresia"],
                request.form["nombre"],
                request.form["duracion_dias"],
                request.form["precio"],
                request.form["id_actividad"]
            )

        elif accion == "eliminar":

            ModeloMembresia.eliminar_membresia(
                request.form["id_membresia"]
            )

        elif accion == "seleccionar":

            membresia_edit = {
                "id_membresia": request.form["id_membresia"],
                "nombre": request.form["nombre"],
                "duracion_dias": request.form["duracion_dias"],
                "precio": request.form["precio"],
                "id_actividad": int(
                    request.form["id_actividad"]
                )
            }

    membresias = ModeloMembresia.obtener_membresias()

    actividades_select = (
        ModeloActividad.obtener_actividades()
    )

    return render_template(
        "interfaz_admin/paneles_ad/reg_membresia/index.html",
        membresias=membresias,
        membresia_edit=membresia_edit,
        actividades_select=actividades_select
    )