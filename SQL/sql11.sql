/*Table structure for table 'autor' */

DROP TABLE IF EXISTS 'autor';

CREATE TABLE autor (
  idautor int NOT NULL IDENTITY,
  nome varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  PRIMARY KEY (idautor)
);
 

insert  into autor(nome,email) values ('J.K.Rowling','jk@hp.com'),('J.R.R.Tolkein','jrr@ceu.com'),('Jorge Amado','ja@ceu.com'),('Machado de Assis','ma@cemiterio.com'),('Suzanne Collins','sc@legal.com');

DROP TABLE Cliente
CREATE TABLE cliente (
  idcliente int NOT NULL IDENTITY,
  nome varchar(100) NOT NULL,
  telefone varchar(45) DEFAULT NULL,
  PRIMARY KEY (idcliente)
);

insert  into cliente(nome,telefone) values ('Joao Silva ','1111'),('Maria Cunha','2222'),('Pedro Aguiar','8888'),('Elaine Luciana','9374'),('Antonio Pereira','3764');

CREATE TABLE escreve (
  idlivro int NOT NULL,
  idautor int NOT NULL,
  PRIMARY KEY (idlivro,idautor)
) ;

insert  into escreve(idlivro,idautor) values (1,5),(2,5),(3,5),(4,1),(5,1);

CREATE TABLE genero (
  idgenero int NOT NULL IDENTITY,
  descricao varchar(100) NOT NULL,
  PRIMARY KEY (idgenero)
);

insert  into genero(descricao) values ('Aventura'),('Fic��o'),('Suspense'),('Romance'),('Infantil'),('Auto-Ajuda');

CREATE TABLE itens_da_venda (
  idvenda int NOT NULL,
  idlivro int NOT NULL,
  qtd int DEFAULT NULL,
  subtotal varchar(45) DEFAULT NULL,
  PRIMARY KEY (idvenda,idlivro)  
);

insert  into itens_da_venda(idvenda,idlivro,qtd,subtotal) values (1,1,1,NULL),(2,1,1,NULL),(3,3,1,NULL),(3,2,1,NULL),(4,4,1,NULL),(5,1,1,NULL),(6,3,1,NULL),(7,5,1,NULL),(8,2,1,NULL),(8,1,1,NULL),(9,4,1,NULL),(10,5,2,NULL);

CREATE TABLE livro (
  idlivro int NOT NULL IDENTITY,
  titulo varchar(100) NOT NULL,
  preco float DEFAULT NULL,
  estoque int DEFAULT '0',
  idgenero int NOT NULL,
  PRIMARY KEY (idlivro,idgenero)
);

insert  into livro(titulo,preco,estoque,idgenero) values ('Jogos Vorazes',25,10,1),('A Esperen�a',35,5,1),('Em Chamas',40,8,1),('Harry Potter e a Pedra Filosofal',20,12,5),('Harry Potter e o Prisioneiro de Azkaban',25,3,5);

CREATE TABLE venda (
  idvenda int NOT NULL IDENTITY,
  data date DEFAULT NULL,
  total float DEFAULT '0',
  idcliente int NOT NULL,
  PRIMARY KEY (idvenda,idcliente)
);

insert  into venda(data,total,idcliente) values ('2012-08-14',0,1),('2012-07-10',0,2),('2012-08-02',0,0),('2012-05-30',0,4),('2011-09-10',0,5),('2011-08-15',0,5);

select * from livro

select 
from livro AS LIVRO where estoque <= 25;

