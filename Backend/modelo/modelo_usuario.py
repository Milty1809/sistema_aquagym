from conexion.conexion import conectar


class ModeloUsuario:

    @staticmethod
    def existe_usuario(username):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc("sp_validar_usuario", [username])

        existe = False

        for resultado in cursor.stored_results():

            if resultado.fetchone():
                existe = True

        cursor.close()
        conexion.close()

        return existe

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

        cursor.close()
        conexion.close()