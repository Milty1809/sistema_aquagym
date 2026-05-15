import os
from flask import Flask
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


# =========================
# IMPORTAR BLUEPRINTS
# =========================
from Backend.controlador.controlador_login import controlador_login
from Backend.controlador.controlador_usuario import controlador_usuario


# =========================
# REGISTRAR BLUEPRINTS
# =========================
app.register_blueprint(controlador_login)
app.register_blueprint(controlador_usuario)


# =========================
# INICIAR SERVIDOR
# =========================
if __name__ == '__main__':
    app.run(debug=True)