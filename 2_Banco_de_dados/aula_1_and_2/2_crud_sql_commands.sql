-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\aula_1_and_2\mydatabase.db

--SELECT usado para selecionar dados especificos ou não de uma tabela no banco de dados

SELECT nome, idade, email FROM usuarioss
WHERE idade > 25
AND idade = 36;



--WHERE passar condição para o SQL, como por exemplo 
--selecione todos os nome, onde (where) a idade é maior
--que 18 (WHERE campo_dade > 18)

--AND serve para extender as condições do WHERE
--Selecionar todas as colunas de uma vez
SELECT * FROM usuarioss
WHERE nome = 'Clarice'
AND idade < 15
AND id > 5;

--modificar dados na tabela
UPDATE usuarioss
set nome = 'test'
WHERE nome = 'Allan';

UPDATE usuarioss
set nome = 'None', idade = 0, email = "00000@000"
WHERE id > 19;


--Deletar dado das tabelas
DELETE FROM usuarioss
WHERE id < 5;


SELECT * FROM usuarioss;
