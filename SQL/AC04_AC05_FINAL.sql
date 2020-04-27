CREATE DATABASE LMS_TESTE;

USE LMS_TESTE;

/* A COMPLETAR - VERIFICAR VALOR DEFAULT */
/* VERIFICAR VALIDAÇÕES DE CAMPO */

CREATE TABLE Usuario
(
ID INT NOT NULL IDENTITY,
Login INT NOT NULL,
Senha VARCHAR(8) NOT NULL,
DtExpiracao DATE DEFAULT '01/01/1900',
CONSTRAINT pkUsuarioID PRIMARY KEY (ID),
CONSTRAINT uqUsuarioLogin UNIQUE (Login)
);

Create table Coordenador
(
ID INT NOT NULL IDENTITY,
Id_usuario INT NOT NULL,
Nome VARCHAR(100),
Email VARCHAR(100) UNIQUE,
Celular INT UNIQUE,
CONSTRAINT pkCoordenadorID PRIMARY KEY (ID),
CONSTRAINT fkCoordenadorId_usuario FOREIGN KEY (Id_usuario) REFERENCES Usuario(ID)
);

create table Aluno(
ID INT NOT NULL IDENTITY,
Id_usuario INT NOT NULL,
Nome VARCHAR(100),
Email VARCHAR(100) UNIQUE,
Celular INT UNIQUE,
RA INT UNIQUE,
Foto VARCHAR(1000),
CONSTRAINT pkAlunoID PRIMARY KEY (ID),
CONSTRAINT fkAlunoId_usuario FOREIGN KEY (Id_usuario) REFERENCES Usuario(ID)
);

Create table Professor(
ID INT NOT NULL IDENTITY,
Id_usuario INT NOT NULL,
Email VARCHAR(100) UNIQUE,
Celular INT UNIQUE,
Apelido VARCHAR(20),
CONSTRAINT pkProfessorID PRIMARY KEY (ID),
CONSTRAINT fkProfessorId_usuario FOREIGN KEY (Id_usuario) REFERENCES Usuario(ID)
);

Create table Disciplina(
ID INT NOT NULL IDENTITY,
Nome VARCHAR(100) UNIQUE,
Data SMALLDATETIME DEFAULT GETDATE(),
Status VARCHAR (10) NOT NULL,
PlanoDeEnsino VARCHAR (5000),
CargaHoraria INT CHECK (CargaHoraria IN (40,80)),
Competencias VARCHAR (5000),
Habilidades VARCHAR (5000),
Ementa VARCHAR (5000),
ConteudoProgramatico VARCHAR (5000),
BibliografiaBasica VARCHAR (5000),
BibliotecaComplementar VARCHAR (5000),
PercentualPratico INT CHECK (PercentualPratico BETWEEN 00 AND 100),
PercentualTeorico INT CHECK (PercentualTeorico BETWEEN 00 AND 100),
IdCoordenador INT NOT NULL,
CONSTRAINT ckStatus CHECK (Status IN ('Aberta','Fechada')),
CONSTRAINT pkDisciplinaID PRIMARY KEY (ID),
CONSTRAINT fkIdCoordenador FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID)
);

create table Curso(
ID INT NOT NULL IDENTITY,
Nome VARCHAR (100) UNIQUE,
CONSTRAINT pkCursoID PRIMARY KEY (ID)
);

Create table DisciplinaOfertada(
ID INT NOT NULL IDENTITY,
IdCoordenador INT NOT NULL,
DtInicioMatricula DATE,
DtFimMatricula DATE,
IdDisciplina INT NOT NULL,
IdCurso INT NOT NULL,
Ano INT CHECK (Ano BETWEEN 1900 AND 2100),
Semestre INT CHECK (Semestre IN (1,2)),
Turma VARCHAR(1) CHECK (Turma BETWEEN 'A' AND 'Z'),
IdProfessor INT NOT NULL,
Metodologia VARCHAR (5000),
Recursos VARCHAR (5000),
CriterioAvaliacao VARCHAR (5000),
PlanoDeAulas VARCHAR (5000),
CONSTRAINT pkDisciplinaOfertadaID PRIMARY KEY (ID),
CONSTRAINT fkDisciplinaOfertadaIdCoordenador FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID),
CONSTRAINT fkDisciplinaOfertadaAtividadeIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID),
CONSTRAINT fkDisciplinaOfertadaIdCurso FOREIGN KEY (IdCurso) REFERENCES Curso(ID),
CONSTRAINT fkDisciplinaOfertadaIdDisciplina FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(ID)
);

Create table SolicitacaoMatricula(
ID INT NOT NULL IDENTITY,
IdAluno INT NOT NULL,
IdDisciplinaOfertada INT NOT NULL,
DtSolicitacao SMALLDATETIME DEFAULT GETDATE(),
IdCoordenador INT NOT NULL,
Status VARCHAR(20) DEFAULT 'SOLICITADA',
CONSTRAINT pkSolicitacaoMatriculaID PRIMARY KEY (ID),
CONSTRAINT ckSMStatus CHECK (Status IN ('SOLICITADA','APROVADA','REJEITADA','CANCELADA')),
CONSTRAINT fkSMIdDisciplinaOfertada FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(ID),
CONSTRAINT fkSMIdCoordenador FOREIGN KEY (IdCoordenador) REFERENCES Professor(ID),
CONSTRAINT fkSMIdAluno FOREIGN KEY (IdAluno) REFERENCES Aluno(ID)
);

Create table Atividade(
ID INT NOT NULL IDENTITY,
Titulo VARCHAR(100) UNIQUE,
Descricao VARCHAR(5000),
Conteudo VARCHAR(5000),
Tipo VARCHAR(20) UNIQUE CHECK (Tipo in ('RESPOSTA ABERTA','TESTE')),
Extras VARCHAR(5000),
IdProfessor INT NOT NULL,
CONSTRAINT pkAtividadeID PRIMARY KEY (ID),
CONSTRAINT fkAtividadeIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID)
);

Create table AtividadeVinculada(
ID INT NOT NULL IDENTITY,
IdAtividade INT NOT NULL,
IdProfessor INT NOT NULL,
IdDisciplinaOfertada INT NOT NULL,
Rotulo VARCHAR(50) UNIQUE,
Status CHAR(20),
DtInicioRespostas DATE,
DtFimRespostas DATE,
CONSTRAINT ckAVStatus CHECK (Status IN ('DISPONIBILIZADA','ABERTA','FECHADA','ENCERRADA','PRORROGADA')),
CONSTRAINT pkAtividadeVinculadaID PRIMARY KEY (ID),
CONSTRAINT fkAtividadeVinculadaIdAtividade FOREIGN KEY (IdAtividade) REFERENCES Atividade(ID),
CONSTRAINT fkAtividadeVinculadaIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID),
CONSTRAINT fkIdAtividadeVinculadaIdDisciplinaOfertada FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(ID)
);

Create table Entrega(
ID INT NOT NULL IDENTITY,
IdAluno INT NOT NULL,
IdAtividadeVinculada INT NOT NULL,
Titulo CHAR(150),
Resposta CHAR(3000),
DtEntrega SMALLDATETIME DEFAULT GETDATE(),
Status CHAR(15) DEFAULT 'ENTREGUE',
IdProfessor INT NOT NULL,
Nota FLOAT,
DtAvaliacao DATE,
Obs CHAR(3000),
CONSTRAINT ckEntregaNota CHECK (Nota BETWEEN 0.00 AND 10.00),
CONSTRAINT ckEntregaStatus CHECK (Status IN ('ENTREGUE','CORRIGIDO')),
CONSTRAINT pkEntregaID PRIMARY KEY (ID),
CONSTRAINT fkEntregaIdAluno FOREIGN KEY (IdAluno) REFERENCES Aluno(ID),
CONSTRAINT fkEntregaIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID),
CONSTRAINT fkEntregaIdAtividadeVinculada FOREIGN KEY (IdAtividadeVinculada) REFERENCES AtividadeVinculada(ID)
);

Create table Mensagem(
ID INT NOT NULL IDENTITY,
IdAluno INT NOT NULL,
IdProfessor INT NOT NULL,
Assunto VARCHAR (150),
Referencia VARCHAR (150),
Conteudo VARCHAR (3000),
Status CHAR(15) DEFAULT 'ENVIADO',
DtEnvio SMALLDATETIME DEFAULT GETDATE(),
DtRespostas DATE,
Resposta DATE,
CONSTRAINT ckMensagemStatus CHECK (Status IN ('ENVIADO','LIDO','RESPONDIDO')),
CONSTRAINT pkMensagemID PRIMARY KEY (ID),
CONSTRAINT fkMensagemIdAluno FOREIGN KEY (IdAluno) REFERENCES Aluno(ID),
CONSTRAINT fkMensagemIdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID)
);

select * from Usuario;