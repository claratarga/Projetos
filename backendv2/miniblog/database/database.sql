CREATE DATABASE miniblog;

USE miniblog;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE postagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conteudo TEXT NOT NULL,
    data_publicacao DATETIME NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome, username, email) VALUES
('Ana Silva', 'ana', 'ana@email.com'),
('Carlos Souza', 'carlos', 'carlos@email.com');

INSERT INTO postagens (conteudo, data_publicacao, usuario_id) VALUES
('Hoje estou estudando Python.', '2026-10-05 10:00:00', 1),
('Comecei meu projeto com Flask.', '2026-10-05 11:00:00', 1),
('Estou aprendendo desenvolvimento web.', '2026-10-05 12:00:00', 2);