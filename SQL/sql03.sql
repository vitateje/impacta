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

