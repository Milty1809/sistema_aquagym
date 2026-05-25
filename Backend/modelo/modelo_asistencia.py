from conexion.conexion import conectar

class ModeloAsistencia:

    @staticmethod
    def obtener_asistencias_cliente(id_cliente):

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
    
    # =========================
    # OBTENER TODAS
    # =========================
    @staticmethod
    def obtener_asistencias():

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT *
        FROM asistencia
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos


    # =========================
    # REGISTRAR
    # =========================
    @staticmethod
    def registrar_asistencia(
        id_cliente,
        fecha,
        hora
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_registrar_asistencia",
            (
                id_cliente,
                fecha,
                hora
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    # =========================
    # EDITAR
    # =========================
    @staticmethod
    def editar_asistencia(
        id_asistencia,
        id_cliente,
        fecha,
        hora
    ):

        conexion = conectar();

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_editar_asistencia",
            (
                id_asistencia,
                id_cliente,
                fecha,
                hora
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    # =========================
    # ELIMINAR
    # =========================
    @staticmethod
    def eliminar_asistencia(
        id_asistencia
    ):

        conexion = conectar();

        cursor = conexion.cursor()

        cursor.callproc(
            "sp_eliminar_asistencia",
            (
                id_asistencia,
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()