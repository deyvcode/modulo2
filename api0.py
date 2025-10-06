import requests
cep=input('Digite seu CEP: ')

dados=requests.get(f'https://viacep.com.br/ws/{cep}/json/')
result = dados.json()

print(result.get('cep'))
print(result.get('logradouro'))
print(result.get('bairro'))
