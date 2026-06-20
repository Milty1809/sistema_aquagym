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
        password,
        rol,
        username
        
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            'sp_registrar_usuario',
            [
                nombre,
                apellido,
                password,
                rol,
                username
                
            ]
        )

        conexion.commit()

        cursor.close()
        conexion.close()

class ModeloUsuario:

    @staticmethod
    def obtener_usuarios():

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuario")

        usuarios = cursor.fetchall()

        cursor.close()
        conexion.close()

        return usuarios


    @staticmethod
    def existe_usuario(usuario):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM usuario WHERE usuario=%s",
            (usuario,)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return resultado is not None


    @staticmethod
    def registrar_usuario(
        nombre,
        apellido,
        password,
        rol,
        usuario
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_insertar_usuario",
            (
                nombre,
                apellido,
                password,
                rol,
                usuario
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def editar_usuario(
        id_usuario,
        nombre,
        apellido,
        password,
        rol,
        usuario
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_editar_usuario",
            (
                id_usuario,
                nombre,
                apellido,
                password,
                rol,
                usuario
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def eliminar_usuario(id_usuario):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_eliminar_usuario",
            (id_usuario,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()