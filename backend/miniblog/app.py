from flask import Flask, render_template
import mysql.connector

from controllers.postagem_controller import postagem_controller

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senhamysql",
    database="miniblog"
)

if conexao.is_connected():
    print("Conectado ao MySQL com sucesso!")

app.register_blueprint(postagem_controller)


@app.route("/")
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)