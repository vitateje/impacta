

create table Funcionario(
Matricula int,
Codigo_Departamento int,
Matricula_Chefia int,
Codigo_Projeto int,
Nome_Funcionario varchar(50)
CONSTRAINT pkFuncionario PRIMARY KEY (Matricula),
CONSTRAINT fkDepto FOREIGN KEY (Codigo_Departamento) REFERENCES Departamento(Codigo_Departamento),
CONSTRAINT fkProj FOREIGN KEY (Codigo_Projeto) REFERENCES Projeto(Codigo_Projeto),
)

create table Departamento (
Codigo_Departamento int,
Nome_Departamento varchar(50)
CONSTRAINT pkDepartamento PRIMARY KEY (Codigo_Departamento)
)

create table Projeto (
Codigo_Projeto int,
Codigo_Departamento int,
Nome_Projeto varchar(50)
CONSTRAINT pkProjeto PRIMARY KEY (Codigo_Projeto)
CONSTRAINT fkDepartamento FOREIGN KEY (Codigo_Departamento) REFERENCES Departamento(Codigo_Departamento)
)

INSERT INTO Funcionario(Matricula, Codigo_Departamento, Matricula_Chefia, Codigo_Projeto, Nome_Funcionario) 
VALUES (1,101,2,1001,'Antonio Jose');

INSERT INTO Funcionario(Matricula, Codigo_Departamento, Matricula_Chefia, Codigo_Projeto, Nome_Funcionario) 
VALUES (2,102,2,1006,'Maria Almeida');

INSERT INTO Departamento(Codigo_Departamento, Nome_Departamento) 
VALUES (101,'Aplica��o');

INSERT INTO Departamento(Codigo_Departamento, Nome_Departamento) 
VALUES (102,'Banco de Dados');

INSERT INTO Projeto(Codigo_Projeto, Codigo_Departamento, Nome_Projeto) 
VALUES (1001, 101, 'Java');

INSERT INTO Projeto(Codigo_Projeto, Codigo_Departamento, Nome_Projeto) 
VALUES (1006, 101, 'SQL');

select * from Funcionario

select * from Departamento

select * from Projeto


		
select Funcionario.*, Departamento.*
FROM Funcionario JOIN Departamento
ON Funcionario.Codigo_Departamento = Departamento.Codigo_Departamento;

select Funcionario.Nome_Funcionario,

(Funcionario.Matricula_Chefia,

Departamento.Nome_Departamento, Projeto.Nome_Projeto
FROM Funcionario JOIN Departamento
ON Funcionario.Codigo_Departamento = Departamento.Codigo_Departamento
JOIN Projeto on Departamento.Codigo_Departamento = Projeto.Codigo_Departamento
