function buscarPostagens() {
    const termo = document.getElementById("termo").value;
    const resultados = document.getElementById("resultados");

    if (termo.trim() === "") {
        resultados.innerHTML = "<p>Digite um termo para pesquisar.</p>";
        return;
    }

    fetch(`/postagens/buscar/${termo}?pagina=1`)
        .then(response => response.json())
        .then(data => {
            resultados.innerHTML = "";

            if (data.resultados.length === 0) {
                resultados.innerHTML = "<p>Nenhuma postagem encontrada.</p>";
                return;
            }

            data.resultados.forEach(postagem => {
                resultados.innerHTML += `
                    <div class="postagem">
                        <div class="usuario">
                            ${postagem.nome} (@${postagem.username})
                        </div>

                        <p>${postagem.conteudo}</p>

                        <div class="data">
                            ${postagem.data_publicacao}
                        </div>
                    </div>
                `;
            });
        })
        .catch(error => {
            resultados.innerHTML = "<p>Erro ao buscar postagens.</p>";
            console.log(error);
        });
}