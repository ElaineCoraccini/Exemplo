-- database: c:\Users\Note-Pisa\Desktop\Exemplo\2_Banco_de_dados\Aula_3_and_4\mydatabase.db

CREATE VIEW SelectProgramadores as
SELECT id, nome, idade, email, linguagem_de_programacao
from Programadores;

--excluindo uma view
--DROP VIEW SelectProgramadores;
drop view SelectProgramadores;

--select * FROM Programadores;
select * FROM SelectProgramadores;

--criando uma nova view
CREATE VIEW ProgramadoresUsuariosEmailMatch as
Select Programadores.nome as Programador,
Programadores.email as EmailMatch,
Usuarios.nome_usu as Usuarios
from Programadores.email INNER JOIN Usuarios
on Programadores.email = Usuarios.email_usu
WHERE nome IS NOT null
ORDER BY nome asc;

-- Chamar a view nova
select * from ProgramadoresUsuariosEmailMatch;