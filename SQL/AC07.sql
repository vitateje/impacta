use LMS_TESTE;
SELECT * FROM Disciplina;
ALTER TABLE Disciplina ADD docente VARCHAR(50);
SELECT * FROM Disciplina;
ALTER TABLE Disciplina DROP COLUMN docente;
SELECT * FROM Disciplina;

ALTER TABLE Coordenador ADD Apelido VARCHAR(50);
INSERT INTO Coordenador(id_usuario, nome, email, celular, Apelido) VALUES(2,'Ana Cristina', 'ana.cristina@faculdadeimpacta.com.br', '11-99988-7766', 'cris');
SELECT * FROM Coordenador;

INSERT INTO usuario(login,senha,DtExpiracao) VALUES('anacristina', '@ana#2018', '31/12/2020');
SELECT * FROM usuario;