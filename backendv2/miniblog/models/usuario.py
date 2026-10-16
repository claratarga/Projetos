import mysql.connector


def buscar_usuario(usuario_id):
    conexao = get_db()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(sql, (usuario_id,))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario

def buscar_usuarios(termo):
    conexao = mysql.connector.connect(
        host="localhost"
        user="root"
        password="senhamysql"
        database="miniblog"
    )

    cursor = conexao.cursor(ditionary=True)

    sql = """
        SELECT id, nome, username, email
        FROM usuarios
        WHERE nome LIKE %s OR username LIKE %s
    """

    busca = "%" + termo + "%"
    cursor.execute(sql, (busca, busca))

    usuarios = cursor.fetchall()

    cursor.close()

    return usuarios