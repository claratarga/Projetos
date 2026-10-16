from flask import Flask, render_template
from conexao import fechar_conexao
from controllers.postagem_controller import postagem_controller

app = Flask(__name__)

app.register_blueprint(postagem_controller)

app.teardown_appcontext(fechar_conexao)


@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
