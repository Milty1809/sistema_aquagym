from conexion.conexion import conectar

class ModeloMembresia:

    @staticmethod
    def obtener_membresias():

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM membresias
            """
        )

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

class ModeloMembresia:


    @staticmethod
    def obtener_membresias():

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT
            m.id_membresia,
            m.nombre,
            m.duracion_dias,
            m.precio,
            m.id_actividad,
            a.nombre AS actividad
        FROM membresias m
        INNER JOIN actividad a
            ON m.id_actividad = a.id_actividad
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos


    @staticmethod
    def registrar_membresia(
        nombre,
        duracion_dias,
        precio,
        id_actividad
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_insertar_membresia",
            (
                nombre,
                duracion_dias,
                precio,
                id_actividad
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def editar_membresia(
        id_membresia,
        nombre,
        duracion_dias,
        precio,
        id_actividad
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_editar_membresia",
            (
                id_membresia,
                nombre,
                duracion_dias,
                precio,
                id_actividad
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def eliminar_membresia(
        id_membresia
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_eliminar_membresia",
            (id_membresia,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()