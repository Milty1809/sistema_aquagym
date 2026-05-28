from flask import Blueprint, render_template, request

from Backend.modelo.modelo_maquinas import ModeloMaquinas


controlador_maquina = Blueprint(
    "controlador_maquina",
    __name__
)


@controlador_maquina.route(
    "/panel_ent/reg_maquinas",
    methods=["GET", "POST"]
)
def reg_maquinas():

    maquina = None

    if request.method == "POST":

        accion = request.form["accion"]

        if accion == "guardar":

            ModeloMaquinas.insertar_maquina(
                request.form["id_actividad"],
                request.form["nombre"],
                request.form["estado"]
            )

        elif accion == "editar":

            ModeloMaquinas.editar_maquina(
                request.form["id_maquina"],
                request.form["id_actividad"],
                request.form["nombre"],
                request.form["estado"]
            )

        elif accion == "eliminar":

            ModeloMaquinas.eliminar_maquina(
                request.form["id_maquina"]
            )

        elif accion == "seleccionar":

            maquina = {
                "id_maquina": request.form["id_maquina"],
                "id_actividad": int(
                    request.form["id_actividad"]
                ),
                "nombre": request.form["nombre"],
                "estado": request.form["estado"]
            }

    maquinas = ModeloMaquinas.listar_maquinas()

    actividades = ModeloMaquinas.listar_actividades()

    return render_template(
        "interfaz_entrenador/paneles_ent/reg_maquinas/index.html",
        maquinas=maquinas,
        maquina=maquina,
        actividades=actividades
    )