from flask import Blueprint, jsonify, request
from models.postagem import buscar_postagens

postagem_controller = Blueprint("postagem_controller", __name__)


@postagem_controller.route("/postagens/buscar/<termo>", methods=["GET"])
def buscar(termo):
    pagina = request.args.get("pagina", default=1, type=int)

    if pagina < 1:
        pagina = 1

    postagens = buscar_postagens(termo, pagina)

    return jsonify({
        "pagina": pagina,
        "resultados": postagens
    })