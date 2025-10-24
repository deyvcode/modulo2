CREATE TABLE Funcionario (
    id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    comissao REAL
);

CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    marca TEXT,
    quantidade_estoque INTEGER
);

CREATE TABLE Venda (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_funcionario INTEGER NOT NULL,
    quantidade_venda INTEGER,
    valor_venda REAL
);