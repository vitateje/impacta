# CLIENT

# modo cliente // consumindo infos de API

import requests
from flask import Flask, jsonify
from requests import api

r = requests.get('https://github.com/timeline.json')
#r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')

print(r.url)

payload = {'key1': 'value1', 'key2': 'value2'} #parametros
r1 = requests.get("http://httpbin.org/get", params=payload) #utilizando params (parametro)

print(r1.url)

print(r.text)

print(r1.status_code)

#  OMDb API - API KEY c8d08b6 

id_filme = 'tt3896198'

#url = f"http://www.omdbapi.com/?i={chave}&apikey=c8d08b6"

url = f"http://127.0.0.1:5002/teste"

retorno = api.get(url).json() # consumo a API Geral

tabela_usuario = retorno # consumo uma lista de usuarios da API e coloco ela em uma variavel

#print(tabela_usuario[0])
print(retorno)

for x in tabela_usuario:
    if x['id'] == 1:
        print( 'Este é o Codigo de Vitor: ',tabela_usuario.index('Vitor'))
    else:
        pass
