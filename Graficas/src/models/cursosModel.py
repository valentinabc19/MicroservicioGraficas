import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cursosdb",
        port=3307
    )

def obtener_notas_estudiante(correo):
    
    cursor = conn.cursor(dictionary=True)
    query = "SELECT nombreCurso, nota, periodo FROM cursos WHERE correoEstudiante = %s"
    cursor.execute(query, (correo,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados
