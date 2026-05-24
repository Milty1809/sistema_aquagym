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