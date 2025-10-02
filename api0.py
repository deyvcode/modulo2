import requests
cep=input('Digite seu CEP: ')

dados=requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(dados.json().get('cep'))
print(dados.json().get('logradouro'))
print(dados.json().get('bairro'))
