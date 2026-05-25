from flask import Blueprint, render_template, request

from Backend.modelo.modelo_asistencia import ModeloAsistencia

controlador_asistencia = Blueprint(
    "controlador_asistencia",
    __name__
)

# =========================
# CLIENTE
# =========================

@controlador_asistencia.route(
    "/panel_cl/asistencias",
    methods=["GET", "POST"]
)
def asistencias_cliente():

    datos = []

    if request.method == "POST":

        id_cliente = request.form["id_cliente"]

        datos = ModeloAsistencia.obtener_asistencias_cliente(
            id_cliente
        )

    return render_template(
        "interfaz_cliente/paneles_cl/asistencias/index.html",
        asistencias=datos
    )


# =========================
# RECEPCIONISTA
# =========================

@controlador_asistencia.route(
    "/panel_rc/reg_asistencia",
    methods=["GET", "POST"]
)
def asistencias_recepcionista():

    asistencia = None

    # =========================
    # POST
    # =========================

    if request.method == "POST":

        accion = request.form["accion"]

        # =====================
        # GUARDAR
        # =====================

        if accion == "guardar":

            id_cliente = request.form["id_cliente"]

            fecha = request.form["fecha"]

            hora = request.form["hora"]

            ModeloAsistencia.registrar_asistencia(
                id_cliente,
                fecha,
                hora
            )

        # =====================
        # SELECCIONAR
        # =====================

        elif accion == "seleccionar":

            asistencia = {

                "id_asistencia":
                request.form["id_asistencia"],

                "id_cliente":
                request.form["id_cliente"],

                "fecha":
                request.form["fecha"],

                "hora":
                request.form["hora"]

            }

        # =====================
        # EDITAR
        # =====================

        elif accion == "editar":

            id_asistencia = request.form[
                "id_asistencia"
            ]

            id_cliente = request.form[
                "id_cliente"
            ]

            fecha = request.form[
                "fecha"
            ]

            hora = request.form[
                "hora"
            ]

            ModeloAsistencia.editar_asistencia(
                id_asistencia,
                id_cliente,
                fecha,
                hora
            )

        # =====================
        # ELIMINAR
        # =====================

        elif accion == "eliminar":

            id_asistencia = request.form[
                "id_asistencia"
            ]

            ModeloAsistencia.eliminar_asistencia(
                id_asistencia
            )

    datos = ModeloAsistencia.obtener_asistencias()

    return render_template(
        "interfaz_recepcionista/paneles_rc/reg_asistencia/index.html",

        asistencias=datos,

        asistencia=asistencia
    )