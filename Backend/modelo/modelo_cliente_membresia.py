from conexion.conexion import conectar


class ModeloCompra:

    # =========================
    # OBTENER MEMBRESIAS BOX
    # =========================

    @staticmethod
    def obtener_membresias_box():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """

        SELECT
            id_membresia,
            nombre,
            precio,
            duracion_dias

        FROM membresias

        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    # =========================
    # OBTENER COMPRAS
    # =========================

    @staticmethod
    def obtener_compras():

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """

        SELECT

            cm.id_cliente_membresia,

            c.id_cliente,
            c.nombre,
            c.apellido,

            m.id_membresia,
            m.nombre AS membresia,

            cm.fecha_inicio,
            cm.fecha_fin,
            cm.estado

        FROM cliente_membresia cm

        INNER JOIN cliente c
        ON cm.id_cliente = c.id_cliente

        INNER JOIN membresias m
        ON cm.id_membresia = m.id_membresia

        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    # =========================
    # OBTENER MEMBRESIA POR ID
    # =========================

    @staticmethod
    def obtener_membresia_por_id(
        id_membresia
    ):

        conexion = conectar()

        cursor = conexion.cursor(
            dictionary=True
        )

        sql = """

        SELECT *
        FROM membresias
        WHERE id_membresia = %s

        """

        cursor.execute(
            sql,
            (id_membresia,)
        )

        dato = cursor.fetchone()

        cursor.close()
        conexion.close()

        return dato

    # =========================
    # REGISTRAR COMPRA
    # =========================

    @staticmethod
    def registrar_compra(

        id_cliente,
        id_membresia,
        fecha_inicio,
        fecha_fin

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_registrar_compra",

            (
                id_cliente,
                id_membresia,
                fecha_inicio,
                fecha_fin
            )

        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # =========================
    # EDITAR COMPRA
    # =========================

    @staticmethod
    def editar_compra(

        id_cliente_membresia,
        id_cliente,
        id_membresia,
        fecha_inicio,
        fecha_fin

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_editar_compra",

            (
                id_cliente_membresia,
                id_cliente,
                id_membresia,
                fecha_inicio,
                fecha_fin
            )

        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # =========================
    # ELIMINAR COMPRA
    # =========================

    @staticmethod
    def eliminar_compra(

        id_cliente_membresia

    ):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.callproc(

            "sp_eliminar_compra",

            (
                id_cliente_membresia,
            )

        )

        conexion.commit()

        cursor.close()
        conexion.close()

    # =========================
    # ACTUALIZAR ESTADOS
    # =========================

    @staticmethod
    def actualizar_estados():

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        UPDATE cliente_membresia

        SET estado = 'Inactivo'

        WHERE fecha_fin < CURDATE()

        """

        cursor.execute(sql)

        conexion.commit()

        cursor.close()
        conexion.close()