from requests import api

cep = "01133-000"
cep = input('Digite o CEP ')
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = api.get(url).json()

logradouro = retorno['logradouro']
cidade = retorno['localidade']
estado = retorno['uf']
print(f"{logradouro} - {cidade} - {estado}")