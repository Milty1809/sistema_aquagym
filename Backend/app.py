import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "Frontend"),
    static_folder=os.path.join(BASE_DIR, "Frontend")
)

app.secret_key = os.getenv("SECRET_KEY")



# IMPORTAR BLUEPRINTS
from Backend.controlador.controlador_login import controlador_login
from Backend.controlador.controlador_usuario import controlador_usuario
from Backend.controlador.controlador_asistencia import controlador_asistencia
from Backend.controlador.controlador_membresia import controlador_membresia
from Backend.controlador.controlador_actividades import controlador_actividades
from Backend.controlador.controlador_clientes import controlador_clientes
from Backend.controlador.controlador_cliente_membresia import controlador_cliente_membresia
from Backend.controlador.controlador_maquina import controlador_maquina
from Backend.controlador.controlador_mantenimiento import controlador_mantenimiento


# REGISTRAR BLUEPRINTS
app.register_blueprint(controlador_login)
app.register_blueprint(controlador_usuario)
app.register_blueprint(controlador_asistencia)
app.register_blueprint(controlador_membresia)
app.register_blueprint(controlador_actividades)
app.register_blueprint(controlador_clientes)
app.register_blueprint(controlador_cliente_membresia)
app.register_blueprint(controlador_maquina)
app.register_blueprint(controlador_mantenimiento)

@app.route("/panel_cl/membresias")
def membresias():
    return render_template(
        "interfaz_cliente/paneles_cl/membresias/index.html"
    )


@app.route("/panel_cl/actividades")
def actividades():
    return render_template(
        "interfaz_cliente/paneles_cl/actividades/index.html"
    )

# INICIAR SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
