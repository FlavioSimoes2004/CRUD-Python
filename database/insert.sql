-- Inserir 5 usuários
INSERT INTO usuario (nome, cpf, email, senha) VALUES
('Ana Silva', '123.456.789-00', 'ana.silva@email.com', 'senha123'),
('Bruno Souza', '987.654.321-00', 'bruno.souza@email.com', 'senha456'),
('Carla Lima', '111.222.333-44', 'carla.lima@email.com', 'senha789'),
('Diego Torres', '555.666.777-88', 'diego.torres@email.com', 'senhaabc'),
('Elisa Costa', '999.888.777-66', 'elisa.costa@email.com', 'senhadef');

-- Inserir 5 funcionários (assumindo que os usuários já tenham IDs 1 a 5)
INSERT INTO funcionario (id_usuario) VALUES
(1);

-- Inserir 5 livros
INSERT INTO livro (nome, genero, autor, descricao, data_publicacao, quantidade) VALUES
('Dom Casmurro', 'Romance', 'Machado de Assis', 'Livro clássico da literatura brasileira', '1899-01-01', 10),
('O Senhor dos Anéis', 'Fantasia', 'J.R.R. Tolkien', 'Trilogia épica de fantasia', '1954-07-29', 5),
('1984', 'Distopia', 'George Orwell', 'Romance distópico e político', '1949-06-08', 8),
('A Revolução dos Bichos', 'Satírico', 'George Orwell', 'Fábula política sobre o totalitarismo', '1945-08-17', 7),
('Cem Anos de Solidão', 'Realismo Mágico', 'Gabriel García Márquez', 'Família Buendía em Macondo', '1967-05-30', 6);

-- Inserir 5 empréstimos (usando usuários 1 a 5 e livros 1 a 5)
INSERT INTO emprestimo (id_usuario, id_livro, data_emprestimo, data_prazo, data_entrega, emprestimo_status) VALUES
(1, 1, '2025-08-01', '2025-08-15', '2025-08-14', 'Entregue'),
(2, 3, '2025-08-05', '2025-08-20', NULL, 'Em andamento'),
(3, 5, '2025-07-25', '2025-08-10', '2025-08-09', 'Entregue'),
(4, 2, '2025-08-10', '2025-08-25', NULL, 'Em andamento'),
(5, 4, '2025-08-12', '2025-08-27', NULL, 'Em andamento');
