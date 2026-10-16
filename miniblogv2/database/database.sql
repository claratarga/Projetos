CREATE DATABASE IF NOT EXISTS miniblog;

USE miniblog;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS postagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conteudo TEXT NOT NULL,
    data_publicacao DATETIME NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome, username, email)
SELECT 'Ana Silva', 'ana', 'ana@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE username = 'ana'
);

INSERT INTO usuarios (nome, username, email)
SELECT 'Carlos Souza', 'carlos', 'carlos@email.com'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE username = 'carlos'
);

INSERT INTO postagens (conteudo, data_publicacao, usuario_id)
SELECT 'Hoje estou estudando Python.', '2026-10-05 10:00:00', id
FROM usuarios
WHERE username = 'ana'
AND NOT EXISTS (
    SELECT 1 FROM postagens
    WHERE conteudo = 'Hoje estou estudando Python.'
);

INSERT INTO postagens (conteudo, data_publicacao, usuario_id)
SELECT 'Comecei meu projeto com Flask.', '2026-10-05 11:00:00', id
FROM usuarios
WHERE username = 'ana'
AND NOT EXISTS (
    SELECT 1 FROM postagens
    WHERE conteudo = 'Comecei meu projeto com Flask.'
);

INSERT INTO postagens (conteudo, data_publicacao, usuario_id)
SELECT 'Estou aprendendo desenvolvimento web.', '2026-10-05 12:00:00', id
FROM usuarios
WHERE username = 'carlos'
AND NOT EXISTS (
    SELECT 1 FROM postagens
    WHERE conteudo = 'Estou aprendendo desenvolvimento web.'
);
