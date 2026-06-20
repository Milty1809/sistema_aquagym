from conexion.conexion import conectar

class ModeloActividad:

    @staticmethod
    def obtener_actividades():

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM actividad
            """
        )

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

class ModeloActividad:

    @staticmethod
    def obtener_actividades():

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM actividad"
        )

        actividades = cursor.fetchall()

        cursor.close()
        conexion.close()

        return actividades


    @staticmethod
    def registrar_actividad(nombre):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_insertar_actividad",
            (nombre,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def editar_actividad(
        id_actividad,
        nombre
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_editar_actividad",
            (
                id_actividad,
                nombre
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    @staticmethod
    def eliminar_actividad(
        id_actividad
    ):

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.callproc(
            "sp_eliminar_actividad",
            (id_actividad,)
        )

        conexion.commit()

        cursor.close()
        conexion.close()