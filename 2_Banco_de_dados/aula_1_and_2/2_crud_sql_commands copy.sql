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
set nome = 'teste'
WHERE nome = 'Ana';

UPDATE usuarioss
set nome = 'None', idade = 0, email = "00000@000"
WHERE id > 19;

-- Ao substituir o 'SELECT *' por 'DELETE', em vez de selecionarmos os dados
-- iremos deletar os mesmos

--Deletar dados das tabelas
DELETE FROM usuarioss
WHERE id < 5;


-- Podemos atualizar mais de uma coluna de uma vez
UPDATE usuarioss 
SET nome = 'Bryan', idade = 70, email = 'bryan@gmail.com' 
HERE id = 1;


-- * é usado para selecionar todas as colunas
-- AND é usado quando queremos passar mais condições no SELECT, além do WHERE

-- Selecionar todas as colunas:
SELECT * FROM usuarios
WHERE nome = 'Bruce'
AND idade = 30
AND email = 'bruce@gmail.com';  

