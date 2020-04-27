
select DISTINCT  
a.nome as nome_autor from 
livro l inner join escreve e  on l.idlivro = e.idlivro 
join autor a on a.idautor = e.idautor where l.estoque=0


select 
c.nome as nome_do_cliente,
l.titulo as Livro_comprado
 from
clienteLivraria c join venda v on v.idcliente = c.idcliente
join itens_da_venda iv on iv.idvenda = v.idvenda
join livro l on iv.idlivro = l.idlivro where l.titulo ='A Esperen�a' 


select DISTINCT
g.descricao
from 
livro l  join escreve e  on l.idlivro = e.idlivro 
join autor a on a.idautor = e.idautor
join genero g on l.idgenero = g.idgenero where a.nome='J.K.Rowling'


select c.nome from
clienteLivraria c join venda v on v.idcliente = c.idcliente
join itens_da_venda iv on iv.idvenda = v.idvenda
join livro l on iv.idlivro = l.idlivro
join escreve e on e.idlivro = l.idlivro
join autor a on a.idautor = e.idautor 
where a.nome ='J.K.Rowling'


select g.descricao as genero,
c.nome as Nome_do_cliente 
 from 
clienteLivraria c join venda v on v.idcliente = c.idcliente
join itens_da_venda iv on iv.idvenda = v.idvenda
join livro l on iv.idlivro = l.idlivro
join genero g on g.idgenero = l.idlivro
where c.nome ='Pedro Aguiar'

select distinct
a.nome as nome_do_autor 
 from 
clienteLivraria c join venda v on v.idcliente = c.idcliente
join itens_da_venda iv on iv.idvenda = v.idvenda
join livro l on iv.idlivro = l.idlivro
join escreve e on e.idlivro = l.idlivro
join autor a on a.idautor = e.idautor
where iv.qtd >= 2


--### Para as quest�es abaixo, combine a consulta com as fun��es MAX, MIN, COUNT, AVG, SUM ###


SELECT l.titulo FROM livro as l  inner join itens_da_venda
as i ON l.idlivro = i.idlivro WHERE qtd = (SELECT max(qtd) from itens_da_venda)


SELECT c.nome FROM livro as l INNER JOIN itens_da_venda as i ON
			  l.idlivro = i.idlivro inner join venda as v ON
			  i.idvenda = v.idvenda inner join clientelivraria as c ON 
			  v.idcliente = c.idcliente
 WHERE preco = (SELECT max(preco) from livro)


select a.nome from livro as l inner join escreve as e on l.idlivro = e.idlivro
				inner join autor as a on a.idautor = e.idautor
  where preco = (select min(preco) from livro)


  SELECT avg(l.preco) FROM livro l inner join genero g on g.idgenero = l.idgenero where g.idgenero = 3
>>>>>>> 542dcf92933a9812f207a9ca79ef88dbca5895f6
