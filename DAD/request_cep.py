from requests import api

cep = "01133-000"  # estático
cep = input('Digite o CEP ')  # dinâmico
url = f"http://viacep.com.br/ws/{cep}/json"  # url que busca o CEP
retorno = api.get(url).json()  # retornando URL em JSON # breakpoint

logradouro = retorno['logradouro']
cidade = retorno['localidade']
estado = retorno['uf']
print(f"{logradouro} - {cidade} - {estado}")
