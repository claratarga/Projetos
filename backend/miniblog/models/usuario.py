import mysql.connector


def buscar_usuario(usuario_id):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senhamysql",
        database="miniblog"
    )

    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(sql, (usuario_id,))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario