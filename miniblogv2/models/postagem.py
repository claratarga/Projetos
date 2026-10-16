from conexao import get_db

def buscar_postagens(termo, pagina):
    conexao = get_db()
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
        INNER JOIN usuarios
            ON postagens.usuario_id = usuarios.id
    """

    if termo:
        sql += " WHERE postagens.conteudo LIKE %s"
        sql += " ORDER BY postagens.data_publicacao DESC LIMIT %s OFFSET %s"

        busca = "%" + termo + "%"
        cursor.execute(sql, (busca, limite + 1, inicio))
    else:
        sql += " ORDER BY postagens.data_publicacao DESC LIMIT %s OFFSET %s"
        cursor.execute(sql, (limite + 1, inicio))

    postagens = cursor.fetchall()

    tem_proxima = len(postagens) > limite
    postagens = postagens[:limite]

    cursor.close()

    return postagens, tem_proxima
