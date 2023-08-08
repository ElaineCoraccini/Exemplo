-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\Aula_3_and_4\mydatabase.db

CREATE TABLE IF NOT EXISTS Programadores (
    id INTEGER PRIMARY KEY,
    nome TEXT(40),
    idade INTEGER,
    email TEXT(40)
);

SELECT * FROM Programadores;

--excluindo tabela
DROP TABLE Programadores;

--Revisão:
--CREATE, DROP, DELETE, INSERT, WHERE, LIKE
--SELECT, AND, COUNT, UPDATE, MAX, MIN, AVG



--INSERIR VALORES
INSERT INTO Programadores (nome, idade, email)
VALUES ('Eliot', 25, 'mr_robot@hacker.tor');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Lulli', 15, 'lulli.bb@gamil.com');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Marina', 18, 'mmrpisa@gmail.com');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Marcelo', 38, 'thor.236@hotmail.com');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Legulas', 10, 'legulas_lindo@hotmail.com');


-- atualizar dados
UPDATE Programadores
SET nome = 'Bruno A', 
idade = 60, 
email = 'bruno@gmail.com'
WHERE nome = 'Legulas'
and id = 10;


SELECT id, nome, idade, email FROM Programadores
WHERE nome = 'Bruno';

--incluindo nova coluna
ALTER TABLE Programadores
ADD COLUMN linguagem_de_programacao TEXT(40);

--inserir as linguagens de programação manualmente para cada linha
UPDATE Programadores
SET linguagem_de_programacao = 'C#'
WHERE id > 5 and id < 9;

--buscar os valores min max, de colunas
SELECT max(id) as id_maior,
min(idade) as idade_menor
FROM Programadores;

--calculando média
SELECT round(avg(idade), 2) as media_idade
FROM Programadores;

--buscar palavras nos baseando em um texto aleatorio
--palavras que começam com B
SELECT * from Programadores
WHERE nome like 'b%';
SELECT * from Programadores
WHERE nome like '%l%';
SELECT * from Programadores
WHERE nome like '%ma%';

--order by = ordene por:
SELECT * FROM Programadores
ORDER BY idade desc;
SELECT * FROM Programadores
ORDER BY idade ASC;
SELECT * FROM Programadores
ORDER BY nome DESC;

--exercicio
--ordene a tabela programadores por todas as colunas usando tanto o desc quanto o asc
SELECT nome FROM Programadores
ORDER BY nome desc;
SELECT nome from Programadores
ORDER BY nome asc;

SELECT id FROM Programadores
ORDER BY id desc;
SELECT id from Programadores
ORDER BY id asc;

SELECT email FROM Programadores
ORDER BY email desc;
SELECT email from Programadores
ORDER BY email asc;

SELECT linguagem_de_programacao FROM Programadores
ORDER BY linguagem_de_programacao desc;
SELECT linguagem_de_programacao from Programadores
ORDER BY linguagem_de_programacao asc;

--group by = agrupe por
SELECT *, count(idade) as quantidade_idade
FROM Programadores
WHERE idade > 18
GROUP BY idade;

SELECT count(linguagem_de_programacao) as total_python
FROM Programadores
WHERE linguagem_de_programacao = 'C++'
GROUP BY linguagem_de_programacao;


--  |--##-- EX: --##--|

-- Criar a coluna salario_dev na tabela Programadores 
--Double usado para numeros quebrados 
ALTER TABLE Programadores
ADD COLUMN salario_dev DOUBLE;

--inserir salarios diferentes para todas as linhas
UPDATE Programadores
SET salario_dev = 5999
WHERE salario_dev is null
and id = 15;

--Em seguida, selecionar os dados ordenando por id
select * from programadores
ORDER BY id desc;

-- Mostrando a média da coluna salario_dev
SELECT round(avg(salario_dev), 2) as media_salario
FROM Programadores;

-- Criar mais 5 colunas em uma das tabelas e inserir os dados manualmente com up date 
ALTER TABLE Programadores
ADD COLUMN Endereco;

ALTER TABLE Programadores
ADD COLUMN Naturalidade;

ALTER TABLE Programadores
ADD COLUMN RG;

ALTER TABLE Programadores
ADD COLUMN CPF;

ALTER TABLE Programadores
ADD COLUMN telefone;

--incluir informações na tabela
UPDATE Programadores
SET Endereco = 'Rua Pedra Preto', Naturalidade = 'Taipa', RG = 123654475, CPF = 12358796, telefone = 998855552
WHERE Endereco is null
and id = 16;

-- Selecionar a maior idade, e o menor id da tabela Programadores
SELECT max(idade) as idade_maior,
min(id) as id_menor
FROM Programadores;

-- Selecionar todas as colunas da tabela Programadores e ordenar pelo nome em ordem alfabética
--DESC/ASC
SELECT * FROM Programadores
ORDER BY Endereco desc;

SELECT * FROM Programadores
ORDER BY Endereco asc;

-- Selecionar o nome e a idade da tabela Programadores, agrupando pela idade = GROUP BY
SELECT nome, idade, count(idade) as total_idades from programadores
GROUP BY idade;

-- mostrando a mesma como total_idade_grup apenas onde a idade é maior ou igual a 18
SELECT nome, idade, count(idade) as total_idade_grup from programadores
WHERE idade > 17
GROUP BY idade;

-- Selecionar todas as colunas da tabela Programadores e ordenando por id em ordem decrescente
SELECT id FROM Programadores
ORDER BY id desc;

--Homework:
-- Criar uma tabela nova, inserir 20 linhas e 8 colunas na tabela
create table if not exists newtable (
    nr_sequencia INTEGER PRIMARY KEY ,
    nome TEXT(40),
    idade INTEGER,
    email TEXT(40),
    nacionalidade TEXT(40),
    endereco TEXT(60),
    num_casa INTEGER,
    religiao TEXT(15),
    cpf INTEGER
);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Anderson', 8, 'deson@gmail.com', 'Brasileiro', 'Rua Argentina', 37, 'Católica', 08876543299);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Clarice', 6, 'clarice@gmail.com', 'Alemã', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Mariazinha', 6, 'ma_22@gmail.com', 'Inglesa', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Clarice', 6, 'clarice@gmail.com', 'Alemã', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Clarice', 6, 'clarice@gmail.com', 'Alemã', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Clarice', 6, 'clarice@gmail.com', 'Alemã', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

INSERT INTO newtable(nome, idade, email, nacionalidade, endereco, num_casa, religiao, cpf)
VALUES ('Clarice', 6, 'clarice@gmail.com', 'Alemã', 'Rua Rio Branco', 7889, 'Logosofia', 12552903889);

-- Refazer todos os exercícios desse arquivo com a tabela criada


