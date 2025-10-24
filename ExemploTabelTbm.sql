INSERT INTO Funcionario (nome, comissao) VALUES
('João Pereira', 6),
('Ana Souza', 5),
('Carlos Lima', 7),
('Júlia Mendes', 6),
('Pedro Santos', 5),
('Maria Silva', 4);

INSERT INTO Produto (nome, marca, quantidade_estoque) VALUES
('Camiseta', 'Nike', 42),
('Calça Jeans', 'Levi’s', 28),
('Jaqueta', 'Adidas', 17),
('Vestido', 'Zara', 22),
('Moletom', 'Puma', 20),
('Saia', 'Renner', 31),
('Boné', 'Oakley', 25);


INSERT INTO Venda (id_produto, id_funcionario, quantidade_venda, valor_venda) VALUES
(1, 1, 18, 2160.00),
(2, 2, 12, 3600.00),
(3, 3, 8, 2800.00),
(4, 4, 15, 4500.00),
(5, 5, 10, 2500.00),
(6, 6, 9, 1350.00);