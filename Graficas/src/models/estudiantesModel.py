import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="usuariosDB",
        port=3307
    )

def obtener_nombre_estudiante(usuario):
    
    cursor = conn.cursor(dictionary=True)
    query = "SELECT correo FROM estudiantes WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados
