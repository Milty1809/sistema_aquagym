from conexion.conexion import conectar


class ModeloMantenimiento:

    @staticmethod
    def mostrar():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """
        SELECT *
        FROM mantenimiento
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    @staticmethod
    def guardar(
        id_maquina,
        fecha,
        descripcion
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_insertar_mantenimiento",
            (
                id_maquina,
                fecha,
                descripcion
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def editar(
        id_mantenimiento,
        id_maquina,
        fecha,
        descripcion
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_editar_mantenimiento",
            (
                id_mantenimiento,
                id_maquina,
                fecha,
                descripcion
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(
        id_mantenimiento
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_eliminar_mantenimiento",
            (
                id_mantenimiento,
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def obtener_maquinas():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """
        SELECT
            id_maquina,
            nombre
        FROM maquinas
        ORDER BY nombre
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos