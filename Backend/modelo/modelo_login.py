from conexion.conexion import conectar


class ModeloLogin:

    @staticmethod
    def iniciar_sesion(
        username,
        password
    ):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.callproc(
            'sp_login',
            [
                username,
                password
            ]
        )

        usuario = None

        for resultado in cursor.stored_results():

            usuario = resultado.fetchone()

        cursor.close()
        conexion.close()

        return usuario