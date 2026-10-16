import mysql.connector
from flask import g

def get_db():
    if "conexao" not in g:
        g.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="senhamysql",
            database="miniblog"
        )

    return g.conexao

def fechar_conexao(exception=None):
    conexao = g.pop("conexao", None)

    if conexao is not None:
        conexao.close()
