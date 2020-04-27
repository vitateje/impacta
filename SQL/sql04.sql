/* NOME_ATRIBUTO - TIPO_ATRIBUTO - TAMANHO_CAMPO - NOT NULL OU DEFAULT - IDENTITY(ID E AUTOINCREMENTO */

CREATE TABLE Prova
(
idProva int IDENTITY (1,1),
Matricula int NOT NULL,
Nota decimal (4,2) NOT NULL,
CONSTRAINT pkProva PRIMARY KEY (idProva),
CONSTRAINT fkProvaMatricula FOREIGN KEY (Matricula) REFERENCES Aluno(Matricula)
);

CREATE TABLE Cliente
(
numcliente int IDENTITY (1,1),
cpf int not null,
rg int not null,
constraint plCliente PRIMARY KEY (numcliente),
constraint uqClientecpf UNIQUE (cpf),
constraint uqClienterg UNIQUE (rg)
);

use fit_alunos;

create table CLIENTE_UP
(
NumCliente int IDENTITY (1,1),
CPF int NOT NULL,
RG int NOT NULL,
CONSTRAINT plCliente PRIMARY KEY (NumCliente),
CONSTRAINT uqClienteCPF UNIQUE (CPF),
CONSTRAINT uqClienteRG UNIQUE (RG)
);

/* Comando para alterar ou adicionar algo na tabela */

ALTER TABLE Cliente ADD CNPJ varchar(20);

/* alterar o nome da tabela */

ALTER TABLE Cliente ALTER COLUMN CNPJ INT;

alter table Cliente DROP Column CNPJ;

CREATE TABLE Veiculo_1801745
(
idVeiculo  INT IDENTITY NOT NULL,
Placa  char (8) NOT NULL,
Marca  varchar (20) NOT NULL,
);

insert into Veiculo_1801745 (Placa,Marca) VALUES ('XPT-7654','Ford');
insert into Veiculo_1801745 (Marca,Placa) VALUES ('GM','KML-7299');
INSERT INTO Veiculo_1801745 VALUES ('EXH-2566','fiat');

select * from Veiculo_1801745;

delete top (1) from Veiculo_1801745;

/* UPDATE */

UPDATE Veiculo_1801745

