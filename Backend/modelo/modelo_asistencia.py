from conexion.conexion import conectar

class ModeloAsistencia:

    @staticmethod
    def obtener_asistencias(id_cliente):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM asistencia
            WHERE id_cliente = %s
            """,
            (id_cliente,)
        )

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos