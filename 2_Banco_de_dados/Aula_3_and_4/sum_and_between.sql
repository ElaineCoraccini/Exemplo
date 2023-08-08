-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\Aula_3_and_4\mydatabase.db

--somando todas as idades
SELECT sum(idade) AS soma_das_idades
FROM Programadores
WHERE idade > 26;

SELECT sum(id) AS soma_dos_ids
FROM Programadores;

--selecionando idades "entre" 25 e 35
SELECT * FROM Programadores
WHERE idade BETWEEN 25 AND 25;

SELECT * FROM Programadores
WHERE idade BETWEEN 10 AND 23;



-- # Exercícios:

-- OBS: Se o exercício pedir por dados que ainda não existem, inserir os mesmos.
    -- Cada nota, corresponderá a uma matéria do aluno, portanto o alunos pode
    -- aparecer mais de um vez na tabela com notas distintas para cada matéria,
    -- no entando deve ter o id único com uma chave primária
    -- Se o exercício estiver muito difícil, pule e volte depois

-- Crie uma tabela chamada "Alunos" com as colunas id como inteiro e chave primária,
-- nome como texto, idade como inteiro, notas como double, matéria como texto.
CREATE TABLE IF NOT EXISTS Alunos (
id INTEGER PRIMARY KEY,
Nome TEXT(40),
Idade INTEGER,
Notas DOUBLE,
Materia TEXT(40)
);

DROP TABLE Alunos;

-- Insira 20 linhas distintas na tabela alunos para cada linha, tente incluir diversidade nas notas e matérias.
INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Ana', 10, 7.0, 'Portugues');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)  -- arrunmar função
VALUES ('Jessica', 20, 8.5, 'Ciencias');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('André', 42, 9.0, 'Matematica');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Renata', 32, 5.0, 'Historia');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Anderson', 25, 7.2, 'Quimica');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Marcio', 28, 8.5, 'Fisica');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Beatriz', 36, 7.0, 'Geografia');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Juliana', 17, 7.2, 'Ingles');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Claudia', 15, 9.2, 'Artes');

INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('Douglas', 18, 2.0, 'Educação Fisica');

-- Selecione todos os registros da tabela "Alunos".
SELECT * FROM Alunos;

-- Selecione apenas o nome e a idade dos alunos da tabela "Alunos".
SELECT Nome, Idade from Alunos;

-- Insira um novo aluno na tabela "Alunos" com nome "João" e idade 25, sem matéria e sem notas.
INSERT INTO Alunos (Nome, Idade, Notas, Materia)
VALUES ('John 5', null, null, 25);

-- Selecione todas as colunas onde a matéria está com valor null.
SELECT * FROM Alunos
WHERE Materia is null;

-- Atualize a idade do aluno com id 10 para 22 anos na tabela "Alunos".
UPDATE Alunos
SET Idade = 22
WHERE id = 10;

-- Selecione a maior idade presente na tabela "Alunos".
SELECT max(Idade) as max_idade from Alunos;

-- Selecione o menor valor da coluna "notas".
SELECT min(Notas) as min_notas from Alunos;

-- Ordene os alunos da tabela "Alunos" por nota em ordem decrescente.
SELECT * FROM Alunos
ORDER BY Notas desc;

-- Calcule a média das notas dos alunos.
SELECT round(avg(notas), 2) as media FROM Alunos;

-- Inserir mais 15 linhas com dados distintos, e modirifcar três linhas existentes em pelo menos duas colunas cada.

INSERT INTO Alunos (nome, notas, materia, idade)
VALUES('William', 2,'História', 14);

-- Crie uma coluna escola e insira as escolas para os alunos usando update 
ALTER TABLE Alunos
ADD COLUMN escola TEXT(70);

UPDATE Alunos
SET escola = 'EEB Carmem Miranda'

-- Selecione os alunos cujo nome começa com a letra "A" na tabela "Alunos".
SELECT nome FROM Alunos
WHERE nome LIKE 'a%';

-- Ordene os alunos da tabela "Alunos" por idade em ordem crescente.
--SELECT * FROM Alunos

SELECT * FROM Alunos
ORDER BY idade ASC;

-- Selecione os alunos que têm idade entre 20 e 25 anos na tabela "Alunos".
SELECT * FROM Alunos
WHERE IDADE BETWEEN 20 AND 25;

-- Selecione os alunos que têm idade maior que 18 e que estudam na escola "Bom Jesus" na tabela "Alunos".
SELECT * FROM Alunos
WHERE idade > 18
AND escola = 'Bom Jesus';

-- Escreva uma consulta SQL que calcule a média de idade dos alunos para cada escola
SELECT AVG(idade) as media_das_idades
from Alunos;

-- Selecione os alunos que obtiveram uma nota maior ou igual a 7 na disciplina de "Matemática".
SELECT * from Alunos
WHERE notas >= 7
and materia = 'Matemática';

-- Selecione os alunos que obtiveram uma nota menor que 5 na disciplina de "História".
SELECT * from Alunos
WHERE notas < 5
AND materia = 'História';

-- Selecione os alunos que têm o nome terminado com a letra "o" na tabela "Alunos".
SELECT * from Alunos
where nome like '%o';

-- Selecione os alunos que estudam na escola "Escola Y" e têm idade menor que 30 anos na tabela "Alunos".
SELECT * from Alunos
where escola = 'Escola Y'
and idade < 30;

-- Selecione os alunos que estudam na escola "Escola Z" ou têm mais de 35 anos na tabela "Alunos".
SELECT * from Alunos
where escola = 'Escola Z'
or idade > 35;

-- Ordene os alunos da tabela "Alunos" por nome em ordem alfabética.
SELECT * from Alunos
order by nome asc;

-- Conte quantos alunos obtiveram a nota máxima na disciplina de "Química".
SELECT count(*) as quantidade_alunos_com_nota_max
FROM Alunos
WHERE Notas = max(nota)
AND materia = 'Quimica';

SELECT COUNT(*) AS obtveram_nota_maxima
FROM Alunos
WHERE nota = (SELECT MAX(nota) FROM Alunos WHERE materia = 'Química')
AND materia = 'Química';

-- Selecione os alunos cujo nome contém a letra "e" e a idade é maior que 25 na tabela "Alunos".

-- Escreva uma consulta SQL que liste o nome do aluno mais velho de cada escola.
