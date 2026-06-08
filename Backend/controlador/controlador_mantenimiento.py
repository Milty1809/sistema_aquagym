from flask import Blueprint, render_template, request

from Backend.modelo.modelo_mantenimiento import ModeloMantenimiento


controlador_mantenimiento = Blueprint(
    "controlador_mantenimiento",
    __name__
)


@controlador_mantenimiento.route(
    "/panel_ent/mantenimiento",
    methods=["GET", "POST"]
)
def mantenimiento():

    mantenimiento_seleccionado = None

    if request.method == "POST":

        accion = request.form["accion"]

        if accion == "guardar":

            ModeloMantenimiento.guardar(
                request.form["id_maquina"],
                request.form["fecha"],
                request.form["descripcion"]
            )

        elif accion == "editar":

            ModeloMantenimiento.editar(
                request.form["id_mantenimiento"],
                request.form["id_maquina"],
                request.form["fecha"],
                request.form["descripcion"]
            )

        elif accion == "eliminar":

            ModeloMantenimiento.eliminar(
                request.form["id_mantenimiento"]
            )

        elif accion == "seleccionar":

            mantenimiento_seleccionado = {

                "id_mantenimiento":
                    request.form["id_mantenimiento"],

                "id_maquina":
                    int(request.form["id_maquina"]),

                "fecha":
                    request.form["fecha"],

                "descripcion":
                    request.form["descripcion"]

            }

    mantenimientos = ModeloMantenimiento.mostrar()

    maquinas = ModeloMantenimiento.obtener_maquinas()

    return render_template(
        "interfaz_entrenador/paneles_ent/mantenimiento/index.html",
        mantenimientos=mantenimientos,
        maquinas=maquinas,
        mantenimiento=mantenimiento_seleccionado
    )