--database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\aula_1_and_2\mydatabase.db

--1.Criar uma base de dados chamada: ​exercicio
--2.Conectar a base criada anteriormente em um arquivo Python
--3.Criar uma tabela chamada ​uzuarios​ (com z mesmo), com a seguinte estrutura:
--a.nome varchar de 20 caracteres
--b.sobrenome de 40 caracteres
--c.idade do tipo inteiro

create table if not exists uzuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT(20),
    sobrenome TEXT(40),
    idade INTEGER
);

--4.Renomeie a tabela ​uzuarios​ para ​usuarios​.
ALTER TABLE uzuarios
RENAME TO usuarios;

--5.Adicione uma coluna e-mail com suporte até 40 caracteres
ALTER TABLE usuarios
ADD COLUMN email TEXT(40);

--6.Exclua a coluna sobrenome
ALTER TABLE usuarios
DROP COLUMN sobrenome;

--7.Cadastre os seguintes dados: Vanessa16vanessa.rosa@gmail.com, Adailton22adailton.mas@yahoo.com
--Andressa36andressa.simas@uol.com.br, Mayra24mayra_antunes@gmail.com
--Cristiane14cris.maya@gmail.com, Carina27carina.almeida@gmail.com
--Clóvis29clovis.simao@hotmail.com, Gabriela23gabriela.bragantino@live.com
--Cibelenullcibele_lins@uol.com.br25

INSERT INTO usuarios (email)
values('Vanessa16vanessa.rosa@gmail.com');
INSERT INTO usuarios (email)
values('Adailton22adailton.mas@yahoo.com');
INSERT INTO usuarios (email)
values('Andressa36andressa.simas@uol.com.br');
INSERT INTO usuarios (email)
values('Mayra24mayra_antunes@gmail.com');
INSERT INTO usuarios (email)
values('Cristiane14cris.maya@gmail.com');
INSERT INTO usuarios (email)
values('Carina27carina.almeida@gmail.com');
INSERT INTO usuarios (email)
values('Clóvis29clovis.simao@hotmail.com');
INSERT INTO usuarios (email)
values('Gabriela23gabriela.bragantino@live.com');
INSERT INTO usuarios (email)
values('Cibelenullcibele_lins@uol.com.br25');

--8.Exiba quantos registros existem na tabela
SELECT count(email) from usuarios;

--9.Exibir a quantidade de usuários com idade até 17 anos
SELECT count(*) FROM usuarios
WHERE idade <= 17;

--10.Retornar a quantidade de usuários com o e-mail ​gmail
SELECT count(*) as contador
FROM usuarios
WHERE email LIKE '%gmail%';

--11.Retornar o nome e a idade da pessoa mais


--12.Retornar os dados do usuário com idade igual a nulo
SELECT count(*) as contador
FROM usuarios
WHERE idade IS NULL;

--13.Alterar para 27 todas as idades nulas
UPDATE usuarios
set idade = 27
WHERE idade is null;

--14.Deletar todos os usuários com idade inferior a 18 anos


--15.Excluir todos os dados da tabela e reiniciar a contabilização


--16.Refazer o processo com os seus próprios nomes, tabelas, dados, mas sem excluir no final. 




--17. Criar um CRUD completo com todos os comandos SQL aprendidos em todas as aulas de banco de dados, para o usuário usar através de opções no terminal,
--  como filtrar/selecionar/deletar/ornedar/adicionar dados, criar tabelas, etc... 
--  O usuário deve apenas informar o número da opção, e o programa manipulará o banco de dados conforme a opção selecionada.
--  Informações importantes:
   -- Usar Python e sqlite (pandas opicional), usar arquivos .sql ou escrever o SQL dentro de (f''' string ''') em Python. (Consultar exemplos se necessário)
   -- Criar uma pasta chamada crud_banco e criar um arquivo administrador.py e base_de_dados.db (nomes opicionais)
   -- O arquivo .py irá manipular a base de dados para o usuário, sem o usuário se procupar com o SQL, que rodará no background.
   -- O programa em Python deve rodar encima de laços de repetições, como while, e validando os dados e nomes das colunas,
  --   tabelas, etc... usando ifs e operadores antes de inserir e alterar os dados de forma decisiva! 
   -- O usuário deve apenas informar a opção que ele quer, como:
        --1 - Calcular média da coluna idade
        --2 - Selecionar todos os dados da tabela por nome da tabela
       -- 3 - Deletar linha por nome
        --4 - Deletar linha por id
       -- 5 - Verificar se letra aparece no começo dos nomes na coluna nome
       -- 6 - Selecionar dados por nome da coluna
       -- 7 - Atualizar dados via nome da tabela e nome da coluna
       -- 8 - etc ...
        
    --OBS: Use a criatividade para as opções, acima são apenas exemplos, e inclua todos os comandos SQL aprendidos como opções.




