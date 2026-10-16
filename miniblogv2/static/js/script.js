let paginaAtual = 1;
let termoAtual = "";

async function buscarTudo(pagina) {
    const campo = document.getElementById("termo");
    const resultadosUsuarios = document.getElementById("resultadosUsuarios");
    const resultadosPostagens = document.getElementById("resultadosPostagens");

    if (pagina === 1) {
        termoAtual = campo.value.trim();
    }

    resultadosPostagens.textContent = "Carregando postagens...";

    try {
        const urlPostagens =
            `/postagens?termo=${encodeURIComponent(termoAtual)}&pagina=${pagina}`;

        const respostaPostagens = await fetch(urlPostagens);

        if (!respostaPostagens.ok) {
            throw new Error("Erro ao buscar postagens");
        }

        const dadosPostagens = await respostaPostagens.json();
        mostrarPostagens(dadosPostagens);

        if (termoAtual !== "") {
            resultadosUsuarios.textContent = "Buscando usuários...";

            const respostaUsuarios = await fetch(
                `/usuarios/buscar/${encodeURIComponent(termoAtual)}`
            );

            if (!respostaUsuarios.ok) {
                throw new Error("Erro ao buscar usuários");
            }

            const dadosUsuarios = await respostaUsuarios.json();
            mostrarUsuarios(dadosUsuarios.resultados);
        } else {
            resultadosUsuarios.innerHTML = "";
        }

    } catch (erro) {
        resultadosPostagens.textContent = "Erro ao carregar postagens.";
        console.log(erro);
    }
}


function mostrarUsuarios(usuarios) {
    const resultados = document.getElementById("resultadosUsuarios");
    resultados.innerHTML = "";

    if (usuarios.length === 0) {
        resultados.textContent = "Nenhum usuário encontrado.";
        return;
    }

    usuarios.forEach(usuario => {
        const card = document.createElement("div");
        card.className = "usuario";

        const nome = document.createElement("div");
        nome.className = "nome";
        nome.textContent = `${usuario.nome} (@${usuario.username})`;

        const email = document.createElement("p");
        email.textContent = usuario.email;

        card.appendChild(nome);
        card.appendChild(email);
        resultados.appendChild(card);
    });
}


function mostrarPostagens(data) {
    const resultados = document.getElementById("resultadosPostagens");
    resultados.innerHTML = "";

    paginaAtual = data.pagina;

    if (data.resultados.length === 0) {
        resultados.textContent = "Nenhuma postagem encontrada.";
    } else {
        data.resultados.forEach(postagem => {
            const card = document.createElement("div");
            card.className = "postagem";

            const autor = document.createElement("div");
            autor.className = "nome";
            autor.textContent = `${postagem.nome} (@${postagem.username})`;

            const conteudo = document.createElement("p");
            conteudo.textContent = postagem.conteudo;

            const dataPublicacao = document.createElement("div");
            dataPublicacao.className = "data";
            dataPublicacao.textContent = postagem.data_publicacao;

            card.appendChild(autor);
            card.appendChild(conteudo);
            card.appendChild(dataPublicacao);

            resultados.appendChild(card);
        });
    }

    document.getElementById("numeroPagina").textContent =
        `Página ${paginaAtual}`;

}


function buscarPostagens(pagina) {
    if (pagina < 1) {
        return;
    }

    buscarTudo(pagina);
}


document.addEventListener("DOMContentLoaded", function() {
    buscarTudo(1);
});
