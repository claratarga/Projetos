import mysql.connector


def buscar_postagens(termo, pagina):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senhamysql",
        database="miniblog"
    )

    cursor = conexao.cursor(dictionary=True)

    limite = 5
    inicio = (pagina - 1) * limite

    sql = """
        SELECT 
            postagens.id,
            postagens.conteudo,
            postagens.data_publicacao,
            usuarios.id AS usuario_id,
            usuarios.nome,
            usuarios.username
        FROM postagens
        INNER JOIN usuarios ON postagens.usuario_id = usuarios.id
        WHERE postagens.conteudo LIKE %s
        ORDER BY postagens.data_publicacao DESC
        LIMIT %s OFFSET %s
    """

    busca = "%" + termo + "%"

    cursor.execute(sql, (busca, limite, inicio))

    postagens = cursor.fetchall()

    cursor.close()
    conexao.close()

    return postagens