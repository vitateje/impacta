/* data query language DQL */

CREATE DATABASE localidade;

USE fit_alunos;

CREATE TABLE uf
(
cd_uf INT NOT NULL,
ds_uf_sigla varchar(2) NOT NULL,
ds_uf_nome varchar(200) NULL,
CONSTRAINT pkcd_uf PRIMARY KEY (cd_uf)
);


CREATE TABLE cidades
(
cd_uf_fk INT NOT NULL,
cd_cidade varchar(10) NOT NULL,
ds_cidade_nome varchar(200) NULL,
CONSTRAINT pkcd_cidade PRIMARY KEY (cd_cidade),
CONSTRAINT fkcd_uf FOREIGN KEY (cd_uf_fk) REFERENCES uf(cd_uf)
);

CREATE TABLE bairros
(
cd_bairro varchar(10) NOT NULL,
cd_cidade_pk varchar(10) NOT NULL,
ds_bairro_nome varchar(200) NULL,
CONSTRAINT pkcd_bairro PRIMARY KEY(cd_bairro),
CONSTRAINT fkcd_cidade FOREIGN KEY(cd_cidade_pk) REFERENCES cidades(cd_cidade)
);

drop TABLE uf;

drop TABLE cidades;

drop TABLE bairros;

/* selecionanda um tabela inteira */

select * from uf;

/*selecionando uma coluna de uma tabela */

select ds_uf_sigla from uf;

select ds_uf_nome, ds_uf_sigla from uf;


select cd_uf, 'Vila Mariana', (cd_uf * 3/4), ds_uf_sigla from uf;

/* Apelido para Tabelas */

select ds_uf_sigla AS Sigla,
ds_uf_nome AS Nome from uf;


/* Where - seleciona uma parte da tabela (parametros) */

select ds_uf_sigla AS Sigla
from uf AS ESTADO where cd_uf >= 10;

select *
from uf AS ESTADO where cd_uf >= 10 and ds_uf_sigla = 'RJ';


select *
from uf AS ESTADO where cd_uf BETWEEN 10 AND 15;

select *
from uf AS ESTADO where cd_uf > 10 and
ds_uf_sigla in ('RJ', 'SP', 'WW');

select *
from uf AS ESTADO where ds_uf_sigla LIKE 'R%' OR ds_uf_sigla LIKE '%A';

select *
from uf AS ESTADO where ds_uf_sigla LIKE 'R%' OR ds_uf_sigla LIKE '%A' 
ORDER BY ds_uf_sigla DESC;






