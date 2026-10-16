import os
import mysql.connector
from flask import g

def get_db():
    if "conexao" not in g:
        g.conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "defaultdb")
        )

    return g.conexao

def fechar_conexao(exception=None):
    conexao = g.pop("conexao", None)

    if conexao is not None:
        conexao.close()
