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