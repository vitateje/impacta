CREATE TABLE uf
( 
  cd_uf INT NOT NULL, 
  ds_uf_sigla varchar(2) NOT NULL, 
  ds_uf_nome varchar(200) NULL,
  CONSTRAINT pkcd_uf PRIMARY KEY (cd_uf)
);


CREATE TABLE cidades
( 
  cd_uf INT NOT NULL, 
  cd_cidade varchar(10) NOT NULL, 
  ds_cidade_nome varchar(200) NULL,
  CONSTRAINT pkcd_cidade PRIMARY KEY (cd_cidade),
  CONSTRAINT fkcd_uf FOREIGN KEY (cd_uf) REFERENCES uf(cd_uf)
);


CREATE TABLE bairros
( 
  cd_bairro varchar(10) NOT NULL, 
  cd_cidade varchar(10) NOT NULL, 
  ds_bairro_nome varchar(200) NULL,
  CONSTRAINT pkcd_bairro PRIMARY KEY (cd_bairro),
  CONSTRAINT fkcd_cidade FOREIGN KEY (cd_cidade) REFERENCES cidades(cd_cidade)
);