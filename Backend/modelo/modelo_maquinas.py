from conexion.conexion import conectar


class ModeloMaquinas:

    @staticmethod
    def listar_maquinas():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """
            SELECT *
            FROM maquinas
        """

        cursor.execute(sql)

        maquinas = cursor.fetchall()

        cursor.close()
        conexion.close()

        return maquinas

    @staticmethod
    def listar_actividades():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """
            SELECT *
            FROM actividad
        """

        cursor.execute(sql)

        actividades = cursor.fetchall()

        cursor.close()
        conexion.close()

        return actividades

    @staticmethod
    def insertar_maquina(
        id_actividad,
        nombre,
        estado
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            'sp_registrar_maquina',
            [
                id_actividad,
                nombre,
                estado
            ]
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def editar_maquina(
        id_maquina,
        id_actividad,
        nombre,
        estado
    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            'sp_editar_maquina',
            [
                id_maquina,
                id_actividad,
                nombre,
                estado
            ]
        )

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_maquina(id_maquina):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(
            'sp_eliminar_maquina',
            [id_maquina]
        )

        conexion.commit()

        cursor.close()
        conexion.close()