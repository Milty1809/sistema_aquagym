from conexion.conexion import conectar

class ModeloUsuario:

    @staticmethod
    def buscar_usuario(username):

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.callproc(
            'sp_buscar_usuario',
            [username]
        )

        usuario = None

        for resultado in cursor.stored_results():
            usuario = resultado.fetchone()

        conexion.close()

        return usuario

    @staticmethod
    def registrar_usuario(
        nombre,
        apellido,
        username,
        rol,
        password
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            'sp_registrar_usuario',
            [
                nombre,
                apellido,
                username,
                rol,
                password
            ]
        )

        conexion.commit()
        conexion.close()