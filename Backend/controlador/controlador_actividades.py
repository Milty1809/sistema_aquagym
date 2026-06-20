from flask import Blueprint, render_template 
from flask import request

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


@controlador_actividades.route(
    '/panel_ad/reg_actividad',
    methods=['GET', 'POST']
)
def reg_actividades():

    actividad_edit = None

    if request.method == 'POST':

        accion = request.form.get('accion')

        if accion == 'guardar':

            ModeloActividad.registrar_actividad(
                request.form['nombre']
            )

        elif accion == 'editar':

            ModeloActividad.editar_actividad(
                request.form['id_actividad'],
                request.form['nombre']
            )

        elif accion == 'eliminar':

            ModeloActividad.eliminar_actividad(
                request.form['id_actividad']
            )

        elif accion == 'seleccionar':

            actividad_edit = {
                'id_actividad':
                request.form['id_actividad'],

                'nombre':
                request.form['nombre']
            }

    actividades = ModeloActividad.obtener_actividades()

    return render_template(
        'interfaz_admin/paneles_ad/reg_actividad/index.html',
        actividades=actividades,
        actividad_edit=actividad_edit
    )