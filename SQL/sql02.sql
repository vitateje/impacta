CREATE TABLE Cliente
(
numcliente int IDENTITY (1,1),
cpf int not null,
rg int not null,
constraint plCliente PRIMARY KEY (numcliente),
constraint uqClientecpf UNIQUE (cpf),
constraint uqClienterg UNIQUE (rg)
);