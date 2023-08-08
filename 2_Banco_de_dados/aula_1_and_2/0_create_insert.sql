-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\aula_1_and_2\mydatabase.db

-- Use the ▷ button in the top right corner to run the entire file.



-- 1 - Criar uma tabela
-- PRIMARY KEY: AUTO INCREMENTA O VALOR QUE ESTÁ NO CAMPO
-- força o campo a não ter valor nulo
-- garantir que cada usuário tenha um valor unico

-- IF NOR EXISTS: garante que a tabela apenas será criada caso 
-- uma tabela com o nome informado não existe!

CREATE TABLE IF NOT EXISTS usuarioss (
    -- CAMPO DO TIPO INTEIRO, COM CHAVE PRIMÁRIA
    id INTEGER PRIMARY KEY, 
    -- Texto usado para campos tipo string
     nome TEXT(100),
     -- INTEGER é usado para campos com numeros inteiros
     idade INTEGER,
     -- o último campo não leva virgula
     email TEXT(100)

);

-- 2 - inserindo dados na tabela criada:
-- INSERT INTO comando SQL para inserir dados nas tabelas

INSERT INTO usuarioss (nome, idade, email)
-- é seguido pela palavra VALUES que armazena os valores nas colunas

VALUES ('Bryan', 25, 'Bryan@gmail.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Allan', 29, 'Allan@gmail.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Aline', 18, 'Aline2@gmail.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Clarice', 06, 'mariachiquinha2@gmail.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Elaine', 36, 'Elaine@gmail.com');

--alterando tabelas
--ALTER TABEL é usado para alterar tabelas
--RENAME TO que renomeia a tabela


ALTER TABLE usuarioss
RENAME TO usuarios;

--ADD COLUMN adiciona uma coluna

ALTER TABLE usuarios
ADD COLUMN coluna_nova;

--DROP COLUNM ('drop' comando perigoso) 
ALTER TABLE usuarios
DROP COLUMN coluna_nova;

-- 4 resetando tabelas 
--DELETE FROM deleta todos os dados da tabela se não
--for passado uma condição especifica
--VACUMM  - zerar o primary key

DELETE FROM usuarios;
VACUUM;

-- 5 Destrind tabelas
DROP TABLE usiarioss;