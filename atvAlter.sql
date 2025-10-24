ALTER TABLE Funcionario
ADD COLUMN cargo TEXT;
UPDATE Funcionario
SET cargo = 'Caixa';


ALTER TABLE Produto
ADD COLUMN material TEXT;
UPDATE Produto
SET material = 'Lã';


ALTER TABLE Venda
ADD COLUMN ganhos INTEGER;
UPDATE Venda
SET ganhos = 163;


ALTER TABLE Venda
DROP COLUMN lucro