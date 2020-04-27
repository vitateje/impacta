select * from uf;

select * from bairros;



select AVG(cd_uf) as 'média',
	   MIN(cd_uf) as 'minimo',
	   SUM(cd_uf) as 'SOMA',
	   COUNT(cd_uf) as 'CONTAGEM',
	   MAX(cd_uf) as 'maximo'
from uf;

select count(cd_cidade) from bairros;

select count(distinct cd_cidade) from cidades; 

select cd_cidade as 'codigo cidade' , 
count(cd_cidade) as 'quantidade bairro'
 from bairros
 GROUP BY cd_cidade
 ORDER BY 'quantidade bairro'; 


