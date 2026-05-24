from flask import Blueprint, render_template, request

from Backend.modelo.modelo_asistencia import ModeloAsistencia

controlador_asistencia = Blueprint(
    "controlador_asistencia",
    __name__
)

# =========================
# MOSTRAR PAGINA
# =========================

@controlador_asistencia.route(
    "/panel_cl/asistencias",
    methods=["GET", "POST"]
)
def asistencias():

    datos = []

    # SI EL USUARIO ENVIA EL FORMULARIO
    if request.method == "POST":

        id_cliente = request.form["id_cliente"]

        datos = ModeloAsistencia.obtener_asistencias(
            id_cliente
        )

    return render_template(
        "interfaz_cliente/paneles_cl/asistencias/index.html",
        asistencias=datos
    )