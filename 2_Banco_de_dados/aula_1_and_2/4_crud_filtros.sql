-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\aula_1_and_2\mydatabase.db

---Selecionando o maior valor da coluna idade


SELECT MAX(idade) FROM usuarioss;

SELECT * FROM usuarioss;

SELECT MIN(idade) FROM usuarioss;

-- Selecionando a média da coluna usando AVG
--AVG = avarege, que é média em pt
--AS = como, traga média como "nome_coluna" com média

select avg(idade) from usuarioss;

select avg(idade) as media_idade from usuarioss;

--COUNT = 

select count(*) as quantidade from usuarioss;

select count(email) as quantidade from usuarioss;

select count(*) from usuarioss
where idade > 18;

select count(*) from usuarioss
where idade < 18;

select count(email) as quantidade_final
from usuarioss
where email is not null;
--IS NOT NULL serve para verificar campos/coluna que
--

insert into usuarioss (nome, idade, email)
values ('kaka', 25, null);

select count(*) as contador
from usuarioss
where email is null;

--LIKE = serve para buscar palavras ou parte de palavras
--para usar o like, precisamos usar o %

--busca letra a no inicio
SELECT nome from usuarioss
where nome like 'a%'; 

--busca letra a no final
SELECT nome from usuarioss
where nome like '%a';

--busca letra a entre a palavra
SELECT nome from usuarioss
where nome like '%a%';



