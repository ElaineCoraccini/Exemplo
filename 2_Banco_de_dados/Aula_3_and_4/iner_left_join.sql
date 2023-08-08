-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\Aula_3_and_4\mydatabase.db

--criar uma tabel usuarios com mesma colunas que programadores
--inserir 10 linhas com dados válidos

CREATE TABLE if NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY,
    nome_usu text(40),
    idade_usu INTEGER,
    email_usu TEXT(40),
    tipo_conta_usu TEXT(40),
    sal_usu DOUBLE
);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Marina', 28, 'marina2@gmail.com', 'Free', 5.000);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Marcelo', 39, 'power2@gmail.com', 'Senior', 9.000);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Alice', 9, 'alice2156@gmail.com', 'Junior', 1.050);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Andre', 40, 'chatomax@gmail.com', 'Free', 5.990);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Clarice', 12, 'florzinhabarbie@gmail.com', 'Junior', 500);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Luana', 25, 'luluzinha@gmail.com', 'Pleno', 5.000);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('joão', 28, 'jojo@gmail.com', 'Free', 2.000);

INSERT INTO Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu,sal_usu)
VALUES ('Maria', 16, 'mariazinha@gmail.com', 'Free', 2.700);


--INNER join é utilizado para combinar as tabelas
--ou seja mostrar os dados de ambas, com filtros
--com base na coluna informada do 'ON'
--excluindo tabela
DROP TABLE Usuários;

-- obter uma lista dos programadores juntamente com os usuarios
-- correspondentes com base em seus endereços de email
SELECT Programadores.nome as nome_Programadores,
Usuarios.nome_usu as nome_usuario,
Programadores.email as email_bateu
from Programadores
INNER JOIN Usuarios
on Programadores.email = Usuarios.email_usu;

--Alterando informações da tabela
UPDATE Usuarios
set email_usu = 'mmrpisa@gmail.com'
WHERE nome_usu = 'Maria';

--realizando o mesmo com a idade
UPDATE Usuarios
set idade_usu = 20
WHERE nome_usu = 'Maria';

SELECT Programadores.nome as nome_Programadores,
Usuarios.nome_usu as nome_usuario,
Programadores.idade as idade_bateu
FROM Programadores
INNER JOIN Usuarios
on Programadores.idade = Usuarios.idade_usu;

-- database: c:\Users\Marina-PC\Desktop\apex_bando_de_dados\aula_3_e_4\mydatabase.db

--  Criar tabela usuarios com mesmas colunas que prograadores
-- inserir 10 linhas com dados validos
CREATE TABLE IF NOT EXISTS Usuarios_novo(
    id INTEGER PRIMARY KEY,
    nome_usu text (40),
    idade_usu integer,
    email_usu TEXT(40),
    tipo_conta_usu TEXT (40),
    sal_usu double
);

INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Marina', 28, 'marinaps21@gmail.com', 'free', 5.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Elaine', 48, 'elaine@gmail.com', 'premium', 5.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Clarice', 13, 'marinaps21@gmail.com', 'Ouro', 5.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Isaias', 53, 'pisaiasias@gmail.com', 'Prata', 15.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Leandro', 32, 'leandro@gmail.com', 'free', 8.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('David', 40, 'david@gmail.com', 'premium', 9.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Cristiano', 56, 'cristiano@gmail.com', 'free', 53.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Mariana', 27, 'marinaps21@gmail.com', 'free', 5.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Marilia', 22, 'marilia@gmail.com', 'premium', 45.000);
INSERT INTO Usuarios_novo (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Anderson', 68, 'andy@gmail.com', 'free', 45.000);

-- obter uma lista dos programadores juntamente com os usuarios
-- correspondentes com base em seus endereços de email

SELECT programadores.nome as nome_programador, 
usuarios_novo.nome_usu as nome_usuario,
programadores.email as email_bateu
FROM programadores 
INNER JOIN Usuarios_novo
ON programadores.email = usuarios.email_usu;

--  O INNER JOIN É UTILIZADO PARA COMBINAR AS TABELAS 
-- OU SEJA MOSTRAR OS DADOS DE AMBAS COM FILTROS
-- COM BASE NA COLUNA INFORMADA DEPOIS DO 'ON'

-- Realizando o mesmo com a idade:

SELECT programadores.idade as idade_programador,
usuarios.idade_usu as idade_usuario,
programadores.nome as nome_programador
--usuarios.nome_usu as nome_usuario
from programadores
inner join usuarios
on programadores.idade = usuarios.idade_usu;

select a.idade, b.idade_usu, a.nome, b.nome_usu
from programadores a,
     usuarios b
where a.idade = b.idade_usu;

SELECT a.salario, b.sal_usu, a.nome, b.nome_usu
from    programadores a,
        usuarios b
where a.salario = b.sal_usu
order by nome desc;

--agora vamos supor que voce deseje obter uma lista de todos
--os programadores e se houver o nome usuario correspondente
--com base no endereço de email

SELECT Programadores.nome as nome_Programadores,
Usuarios.nome_usu as nome_usuario
--Programadores.email as email_pro --(esta função tras as informações do e-mail)
from Programadores
LEFT join Usuarios
on Programadores.email = Usuarios.email_usu;  


-- |--- EX 2 ---|
-- Criar tabela Contatos com mesmas colunas que Usuarios + coluna telefone (e outras se desejado)
-- Insira 20 linhas na tabela Contatos e repita o exercícios anterior
-- trocando a tabela usuarios pela tabela contatos*

--criar tabela contatos
CREATE TABLE if NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY,
    nome text(40),
    telefone INTEGER,
    email TEXT(40),
    logradouro TEXT(40),
    numero INTEGER,
    CEP double
);

--excluindo tabela
--DROP TABLE Contatos;

--inserir dados em contatos
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Clarice', 998992325, 'florzinhabarbie@gmail.com', 'Rua Brasil', 500, 89089.239);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Maria', 990092389, 'ma12345678@gmail.com', 'Rua Marginal 12', 1520, 89089.232);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('André', 998992325, 'chatomaxpro@gmail.com', 'Rua Tocantins', 590, 89089.233);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Rogério', 998992322, 'rogerio3@gmail.com', 'BR 470', 60, 89089.235);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Marcio', 90890025, 'mrbison@gmail.com', 'Av Atlantica', 10, 89089.238);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Julia', 998112320, 'juju89@gmail.com', 'Rua Antonio da Veiga', 5, 89089.237);
INSERT INTO Contatos (nome, telefone, email, logradouro, numero, CEP)
VALUES ('Marcilio', 998993335, 'macor12@gmail.com', 'Rua Jardim Brasil', 147, 89089.231);

--repetir exercicios acima com left e inner join
--trocando a tabela usuarios por contatos recem criada
--LEFT
SELECT Contatos.nome as nome_Contatos,
Usuarios.nome_usu as nome_usuario
from Contatos
LEFT join Usuarios
on Contatos.nome = Usuarios.nome_usu;  

--INNER
SELECT Contatos.nome as nome_Cadastro,
Usuarios.nome_usu as nome_usuario
FROM Contatos
INNER JOIN Usuarios
on Contatos.nome = Usuarios.nome_usu;

--Incluindo nova coluna na tabela
ALTER TABLE Contatos
ADD COLUMN ativo boolean;

-- Metade das linhas das duas tabelas tem que estar com o ativo sendo true, e a outra metade false
update contatos
set situacao = False
where id <= 10;

update usuarios
set situacao_usu = true
where id > 5;

-- A consulta deve retornar apenas os usuarios que possuem um id na tabela 
-- contatos correspondente ao id da tabela usuarios.
select  usuarios.id as id_usuario,
        usuarios.nome_usu as nome_usuario,
        contatos.id as id_contato,
        contatos. nome_ctt as nome_contato
from usuarios left join contatos
on usuarios.id = contatos.id;

-- Após o ON, adicione um where no final para adicionar ao filtro também
-- apenas as idades que são maiores que 18 e menores que 30
select Usuarios.nome_usu as nome_usuario,
Contatos.nome as nome_contato,
Usuarios.id as id_bateu
from Usuarios inner join Contatos
on Usuarios.id = Contatos.id
where Usuarios.idade_usu between 18 and 30
and Contatos.idade between 18 and 30
order by Usuarios.nome_usu asc;

-- No Final ordene por nome

SELECT * from Contatos;

UPDATE Usuarios
set ativo = true
WHERE id < 3;

SELECT Usuarios.nome_usu as nome_usuario,
Contatos.nome as nome_contato,
Usuarios.id as id_bateu






