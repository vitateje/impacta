/* NOME_ATRIBUTO - TIPO_ATRIBUTO - TAMANHO_CAMPO - NOT NULL OU DEFAULT - IDENTITY(ID E AUTOINCREMENTO */




CREATE TABLE Prova
(
idProva int IDENTITY (1,1),
Matricula int NOT NULL,
Nota decimal (4,2) NOT NULL,
CONSTRAINT pkProva PRIMARY KEY (idProva),
CONSTRAINT fkProvaMatricula FOREIGN KEY (Matricula) REFERENCES Aluno(Matricula)
);

