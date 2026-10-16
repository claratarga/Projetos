from flask import Blueprint, jsonify, request

from models.postagem import buscar_postagens
from models.usuario import buscar_usuarios

postagem_controller = Blueprint("postagem_controller", __name__)


@postagem_controller.route("/postagens", methods=["GET"])
def listar_postagens():
    termo = request.args.get("termo", "").strip()
    pagina = request.args.get("pagina", default=1, type=int)

    if pagina < 1:
        pagina = 1

    postagens, tem_proxima = buscar_postagens(termo, pagina)

    return jsonify({
        "pagina": pagina,
        "resultados": postagens,
        "tem_proxima": tem_proxima
    })


@postagem_controller.route("/usuarios/buscar/<termo>", methods=["GET"])
def buscar_usuario_por_termo(termo):
    usuarios = buscar_usuarios(termo)

    return jsonify({
        "resultados": usuarios
    })
