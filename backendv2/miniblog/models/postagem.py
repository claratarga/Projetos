import mysql.connector
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
        INNER JOIN usuarios ON postagens.usuario_id = usuarios.id
        WHERE postagens.conteudo LIKE %s
        ORDER BY postagens.data_publicacao DESC
        LIMIT %s OFFSET %s
    """

    busca = "%" + termo + "%"

    cursor.execute(sql, (busca, limite, inicio))

    postagens = cursor.fetchall()

    cursor.close()

    return postagens