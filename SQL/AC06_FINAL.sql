create database AC06SQL;

USE fit_alunos;

drop table Fornecedor;

create table Cor(
    idCor int,
    Descricao VARCHAR(50),
    CONSTRAINT pkidCor PRIMARY KEY (idCor)
);


create table Fornecedor(
    idFornecedor int,
    nome VARCHAR(50),
    telefone VARCHAR (9),
    contato VARCHAR (50),
    CONSTRAINT pk_Fornecedor PRIMARY KEY (idFornecedor)
);


create table Produto(
    idProduto int,
    codigo CHAR(6),
    nome VARCHAR(50),
    estoque int,
    descontinuado TINYINT,
    idFornecedor int,
    idCor int,
    CONSTRAINT pk_Produto PRIMARY KEY (idProduto),
    CONSTRAINT fk_Fornecedor FOREIGN KEY (idFornecedor) REFERENCES Fornecedor(idFornecedor),
    CONSTRAINT fk_Cor FOREIGN KEY (idCor) REFERENCES Cor (idCor)
);


INSERT INTO Cor (idCor, Descricao) VALUES (1,'Branco');
INSERT INTO Cor (idCor,Descricao) VALUES (2,'Preto');
INSERT INTO COR (idCor,Descricao) VALUES (3,'Azul');
INSERT INTO COR (idCor,Descricao) VALUES (4,'Vermelho');
INSERT INTO COR (idCor,Descricao) VALUES (5,'Amarelo');

INSERT INTO Fornecedor (idFornecedor,nome,telefone,contato) VALUES (1,'Sony','8498-8732','Allan');
INSERT INTO Fornecedor (idFornecedor,nome,telefone,contato) VALUES (2,'Motorola','7987-9900','Cristina');
INSERT INTO Fornecedor (idFornecedor,nome,telefone,contato) VALUES (3,'Asus','5476-1120','Felipe');
INSERT INTO Fornecedor (idFornecedor,nome,telefone,contato) VALUES (4,'Nokia','6755-5656','Fabio');

INSERT INTO Produto (idProduto,codigo,nome,estoque,descontinuado,idFornecedor,idCor) VALUES (1,'XT890A','Asus Zenfone',5,0,3,4);
INSERT INTO Produto (idProduto,codigo,nome,estoque,descontinuado,idCor) VALUES (2,'RQ765B','Iphone',0,1,4);
INSERT INTO Produto (idProduto,codigo,nome,estoque,descontinuado,idFornecedor) VALUES (3,'WD528B','Moto X',3,0,2);
INSERT INTO Produto (idProduto,codigo,nome,estoque,descontinuado,idFornecedor,idCor) VALUES (4,'TF897A','Xperia',7,0,1,1);
INSERT INTO Produto (idProduto,codigo,nome,estoque,descontinuado,idFornecedor,idCor) VALUES (5,'RF212B','Moto Maxx',2,0,2,1);

select idProduto from Produto where idProduto > 8;

select * from Produto;

select Produto.codigo, Produto.nome as 'Nome do Produto', Produto.estoque,
		Fornecedor.nome, Fornecedor.contato, Fornecedor.telefone
FROM Produto JOIN Fornecedor
ON Produto.idFornecedor = Fornecedor.idFornecedor;

select Produto.codigo, Produto.nome as 'Nome do Produto', Produto.estoque,
		Fornecedor.nome, Fornecedor.contato, Fornecedor.telefone, Cor.Descricao
FROM Produto JOIN Fornecedor 
ON Produto.idFornecedor = Fornecedor.idFornecedor
JOIN Cor ON Cor.idCor = Produto.idCor;	

select * from Cor;