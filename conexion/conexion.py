import mysql.connector

conexion = mysql.connector.connect(user='root', password='', host='localhost', database='bd2_grupo12', port=3306)
print(conexion)