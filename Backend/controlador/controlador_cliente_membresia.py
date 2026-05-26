from flask import Blueprint, render_template, request

from datetime import datetime, timedelta

from Backend.modelo.modelo_cliente_membresia import ModeloCompra
from Backend.modelo.modelo_clientes import ModeloClientes
from Backend.modelo.modelo_membresia import ModeloMembresia

controlador_cliente_membresia = Blueprint(
    "controlador_cliente_membresia",
    __name__
)

@controlador_cliente_membresia.route(
    "/panel_rc/reg_compra",
    methods=["GET", "POST"]
)
def compras():

    compra = None

    # =========================
    # POST
    # =========================

    if request.method == "POST":

        accion = request.form["accion"]

        # =====================
        # GUARDAR
        # =====================

        if accion == "guardar":

            id_cliente = request.form[
                "id_cliente"
            ]

            id_membresia = request.form[
                "id_membresia"
            ]

            fecha_inicio = request.form[
                "fecha_inicio"
            ]

            membresia = ModeloCompra.obtener_membresia_por_id(
                id_membresia
            )

            dias = membresia[
                "duracion_dias"
            ]

            fecha_inicio_date = datetime.strptime(
                fecha_inicio,
                "%Y-%m-%d"
            )

            fecha_fin = fecha_inicio_date + timedelta(
                days=dias
            )

            fecha_fin = fecha_fin.strftime(
                "%Y-%m-%d"
            )

            ModeloCompra.registrar_compra(
                id_cliente,
                id_membresia,
                fecha_inicio,
                fecha_fin
            )

        # =====================
        # SELECCIONAR
        # =====================

        elif accion == "seleccionar":

            id_membresia = request.form[
                "id_membresia"
            ]

            fecha_inicio = request.form[
                "fecha_inicio"
            ]

            membresia = ModeloCompra.obtener_membresia_por_id(
                id_membresia
            )

            dias = membresia[
                "duracion_dias"
            ]

            fecha_inicio_date = datetime.strptime(
                fecha_inicio,
                "%Y-%m-%d"
            )

            fecha_fin = fecha_inicio_date + timedelta(
                days=dias
            )

            fecha_fin = fecha_fin.strftime(
                "%Y-%m-%d"
            )

            compra = {

                "id_cliente_membresia":
                request.form[
                    "id_cliente_membresia"
                ],

                "id_cliente":
                request.form[
                    "id_cliente"
                ],

                "id_membresia":
                request.form[
                    "id_membresia"
                ],

                "fecha_inicio":
                fecha_inicio,

                "fecha_fin":
                fecha_fin

            }

        # =====================
        # EDITAR
        # =====================

        elif accion == "editar":

            id_cliente_membresia = request.form[
                "id_cliente_membresia"
            ]

            id_cliente = request.form[
                "id_cliente"
            ]

            id_membresia = request.form[
                "id_membresia"
            ]

            fecha_inicio = request.form[
                "fecha_inicio"
            ]

            membresia = ModeloCompra.obtener_membresia_por_id(
                id_membresia
            )

            dias = membresia[
                "duracion_dias"
            ]

            fecha_inicio_date = datetime.strptime(
                fecha_inicio,
                "%Y-%m-%d"
            )

            fecha_fin = fecha_inicio_date + timedelta(
                days=dias
            )

            fecha_fin = fecha_fin.strftime(
                "%Y-%m-%d"
            )

            ModeloCompra.editar_compra(
                id_cliente_membresia,
                id_cliente,
                id_membresia,
                fecha_inicio,
                fecha_fin
            )

        # =====================
        # ELIMINAR
        # =====================

        elif accion == "eliminar":

            id_cliente_membresia = request.form[
                "id_cliente_membresia"
            ]

            ModeloCompra.eliminar_compra(
                id_cliente_membresia
            )

    compras = ModeloCompra.obtener_compras()

    clientes = ModeloClientes.obtener_clientes()

    membresias = ModeloMembresia.obtener_membresias()

    return render_template(
        "interfaz_recepcionista/paneles_rc/reg_compra/index.html",

        compras=compras,

        clientes=clientes,

        membresias=membresias,

        compra=compra
    )