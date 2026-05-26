from conexion.conexion import conectar

class ModeloClientes:


    # =========================
    # OBTENER CLIENTES
    # =========================

    @staticmethod
    def obtener_clientes():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """
        SELECT *
        FROM cliente
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos


    # =========================
    # REGISTRAR CLIENTE
    # =========================

    @staticmethod
    def registrar_cliente(

        nombre,
        apellido,
        ci

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_registrar_cliente",

            (
                nombre,
                apellido,
                ci
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    # =========================
    # EDITAR CLIENTE
    # =========================

    @staticmethod
    def editar_cliente(

        id_cliente,
        nombre,
        apellido,
        ci

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_editar_cliente",

            (
                id_cliente,
                nombre,
                apellido,
                ci
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()


    # =========================
    # ELIMINAR CLIENTE
    # =========================

    @staticmethod
    def eliminar_cliente(

        id_cliente

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_eliminar_cliente",

            (
                id_cliente,
            )
        )

        conexion.commit()

        cursor.close()
        conexion.close()