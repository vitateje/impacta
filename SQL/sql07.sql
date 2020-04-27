

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


INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (1, 'AC', 'Acre');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (2, 'AL', 'Alagoas');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (3, 'AM', 'Amazonas');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (4, 'AP', 'Amap�');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (5, 'BA', 'Bahia');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (6, 'CE', 'Cear�');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (7, 'DF', 'Distrito Federal');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (8, 'ES', 'Esp�rito Santo');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (9, 'GO', 'Goi�s');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (10, 'MA', 'Maranh�o');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (11, 'MG', 'Minas Gerais');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (12, 'MS', 'Mato Grosso do Sul');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (13, 'MT', 'Mato Grosso');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (14, 'PA', 'Par�');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (15, 'PB', 'Para�ba');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (16, 'PE', 'Pernambuco');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (17, 'PI', 'Piau�');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (18, 'PR', 'Paran�');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (19, 'RJ', 'Rio de Janeiro');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (20, 'RN', 'Rio Grande do Norte');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (21, 'RO', 'Rond�nia');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (22, 'RR', 'Roraima');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (23, 'RS', 'Rio Grande do Sul');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (24, 'SC', 'Santa Catarina');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (25, 'SE', 'Sergipe');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (26, 'SP', 'S�o Paulo');

INSERT INTO uf
 (cd_uf, ds_uf_sigla, ds_uf_nome)
VALUES (27, 'TO', 'Tocantins');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (2, '180', 'Taboquinha (Arapiraca)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (5, '362', 'Ant�nio Cardoso');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (5, '537', 'Conde');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (5, '719', 'Itapora (Muritiba)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (5, '895', 'Paiol (Jacaraci)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (5, '1067', 'Tanquinho do Po�o (Andorinha)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (6, '1241', 'Calaba�a (V�rzea Alegre)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (6, '1415', 'Itai�aba');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (6, '1585', 'Paripueira (Beberibe)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (6, '1748', 'Trapi� (Sobral)');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (8, '1916', 'Jer�nimo Monteiro');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (9, '243', 'Apor�');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (9, '109', 'Orizona');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (10, '30', 'Coroat�');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (10, '135', 'Z� Doca');

INSERT INTO cidades
  (cd_uf, cd_cidade, ds_cidade_nome)
VALUES (11, '16', 'Bonfim');


INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('1', '16', 'Abrah�o Alab');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('2', '16', 'Adalberto Arag�o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('3', '16', 'Aeroporto Velho');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('4', '16', 'Alegria');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('5', '16', 'Areal');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('6', '16', 'Avi�rio');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('7', '16', 'Bahia');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('8', '16', 'Bahia Nova');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('9', '16', 'Baixa da Colina');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('10', '16', 'Base');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('11', '16', 'Bela Vista');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('12', '16', 'Bosque');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('13', '16', 'Cadeia Nova');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('14', '16', 'Cadeia Velha');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('15', '16', 'Calafate');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('16', '16', 'Capoeira');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('17', '16', 'Centro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('18', '16', 'Cer�mica');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('19', '16', 'Ch�cara Ip�');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('20', '16', 'Conquista');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('21', '16', 'Corrente');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('22', '16', 'Distrito Industrial');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('23', '16', 'Esperan�a');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('24', '16', 'Esta��o Experimental');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('25', '16', 'Floresta');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('26', '16', 'Geraldo Fleming');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('27', '16', 'Ipase');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('28', '16', 'Ivete Vargas');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('29', '16', 'Izaura Parente');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('30', '16', 'Jardim de Alah');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('31', '16', 'Jardim Europa');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('32', '16', 'Jos� Augusto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('33', '16', 'Jo�o Eduardo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('34', '16', 'Manoel Juli�o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('35', '16', 'Mascarenhas de Moraes');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('36', '16', 'Morada do Sol');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('37', '16', 'Nova Esta��o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('38', '16', 'Novo Horizonte');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('39', '16', 'Palheiral');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('40', '16', 'Papouco');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('41', '16', 'Placas');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('42', '16', 'Pl�cido de Castro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('43', '16', 'Prevent�rio');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('44', '16', 'Primavera');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('45', '16', 'Quinze');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('46', '16', 'Santa In�s');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('47', '16', 'Santa Quit�ria');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('48', '16', 'S�o Francisco');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('49', '16', 'Segundo Distrito');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('50', '16', 'Seis de Agosto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('51', '16', 'Sobral');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('52', '16', 'Tancredo Neves');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('53', '16', 'Taquari');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('54', '16', 'Terminal Cadeia Velha');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('55', '16', 'Tri�ngulo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('56', '16', 'Tropical');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('57', '16', 'Vila Acre');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('58', '16', 'Vila Ivonete');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('59', '30', 'Alto do Cruzeiro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('60', '30', 'Baixa Grande');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('61', '30', 'Baix�o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('62', '30', 'Boa Vista');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('63', '30', 'Bras�lia');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('64', '30', 'Brasiliana');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('65', '30', 'Cacimbas');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('66', '30', 'Caititus');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('67', '30', 'Canaf�stula');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('68', '30', 'Capiat�');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('69', '30', 'Cavaco');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('70', '30', 'Centro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('71', '30', 'Eldorado');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('72', '30', 'Guaribas');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('73', '30', 'Itapo�');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('74', '30', 'Jardim Esperan�a');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('75', '30', 'Jardim Tropical');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('76', '30', 'Manoel Teles');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('77', '30', 'Nova Esperan�a');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('78', '30', 'Novo Horizonte');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('79', '30', 'Olho D''�gua dos Cazuzinhos');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('80', '30', 'Ouro Preto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('81', '30', 'Planalto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('82', '30', 'Z�lia Barbosa Rocha');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('83', '30', 'Primavera');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('84', '30', 'Santa Edwiges');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('85', '30', 'Santa Esmeralda');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('86', '30', 'S�o Luiz');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('87', '30', 'Senador Arnon de Melo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('88', '30', 'Senador Teot�nio Vilela');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('89', '30', 'Verdes Campos');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('90', '109', 'Santos Dumont');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('91', '109', 'Antares');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('92', '109', 'Barro Duro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('93', '109', 'Bebedouro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('95', '109', 'Benedito Bentes');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('96', '109', 'Bom Parto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('97', '109', 'Cana�');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('98', '109', 'Centro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('99', '109', 'Ch� da Jaqueira');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('100', '109', 'Cruz das Almas');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('101', '109', 'Farol');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('102', '109', 'Feitosa');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('103', '109', 'Fern�o Velho');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('104', '109', 'Ipioca');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('105', '109', 'Gruta de Lourdes');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('107', '109', 'Jacarecica');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('108', '109', 'Jacintinho');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('109', '109', 'Jaragu�');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('110', '109', 'Jati�ca');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('111', '109', 'Levada');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('112', '109', 'Mangabeiras');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('113', '109', 'Mutange');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('114', '109', 'Ouro Preto');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('115', '109', 'Paju�ara');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('116', '109', 'Pinheiro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('117', '109', 'Pitanguinha');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('118', '109', 'Po�o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('119', '109', 'Ponta da Terra');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('120', '109', 'Ponta Grossa');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('121', '109', 'Ponta Verde');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('122', '109', 'Pontal da Barra');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('123', '109', 'Prado');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('124', '109', 'Riacho Doce');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('125', '109', 'Rio Novo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('126', '109', 'Santa Am�lia');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('128', '109', 'Serraria');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('129', '109', 'Tabuleiro do Martins');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('130', '109', 'Trapiche da Barra');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('131', '109', 'Vergel do Lago');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('132', '135', 'Alto do Cruzeiro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('133', '135', 'Centro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('134', '135', 'Eucal�ptos');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('135', '135', 'Jardim Brasil');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('136', '135', 'Juca Sampaio');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('137', '135', 'Palmeira de Fora');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('138', '135', 'Para�so');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('139', '135', 'Ribeira');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('140', '135', 'S�o Crist�v�o');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('141', '135', 'S�o Francisco');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('142', '135', 'Ten�rio Cavalcante');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('144', '135', 'Vila Maria');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('145', '135', 'Vila Nova');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('146', '135', 'Xucurus');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('147', '243', 'Adrian�polis');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('148', '243', 'Aleixo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('149', '243', 'Alvorada');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('150', '243', 'Aparecida');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('151', '243', 'Armando Mendes');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('152', '243', 'Bet�nia');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('153', '243', 'Cachoeirinha');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('154', '243', 'Centro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('155', '243', 'Chapada');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('156', '243', 'Cidade Nova');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('157', '243', 'Col�nia Ant�nio Aleixo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('158', '243', 'Col�nia Oliveira Machado');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('159', '243', 'Col�nia Santo Ant�nio');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('160', '243', 'Col�nia Terra Nova');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('161', '243', 'Compensa');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('162', '243', 'Coroado');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('163', '243', 'Crespo');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('164', '243', 'Distrito Industrial');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('165', '243', 'Dom Pedro');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('166', '243', 'Educandos');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('167', '243', 'Flores');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('168', '243', 'Gl�ria');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('169', '243', 'Japiim');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('170', '243', 'Jorge Teixeira');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('171', '243', 'L�rio do Vale');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('172', '243', 'Mauazinho');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('173', '243', 'Monte das Oliveiras');

INSERT INTO bairros
  (cd_bairro, cd_cidade, ds_bairro_nome)
VALUES ('174', '243', 'Morro da Liberdade');

select * from uf;