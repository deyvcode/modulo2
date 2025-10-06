import requests

dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante')
result = dados.json()

for i in result:
    print(i.get('Bebida'))
