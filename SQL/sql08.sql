select cidades.ds_cidade_nome, uf.ds_uf_sigla
from uf JOIN cidades
ON uf.cd_uf = cidades.cd_uf


select uf.ds_uf_sigla, cidades.ds_cidade_nome
from cidades JOIN uf
ON  cidades.cd_uf = uf.cd_uf;


select cidades.*, uf.*
from uf JOIN cidades
ON uf.cd_uf = cidades.cd_uf;

select * from cidades;

select * from bairros;

/* left join = traz tudo do lado esquerdo */

/* right join = traz tudo da tabela da direita */

select bairros.*, cidades.*
from bairros left JOIN cidades
ON cd_bairro = ds_cidade_nome;

select bairros.*, cidades.*
from bairros FULL JOIN cidades
ON b_cidade_nome = cidade_nome;


