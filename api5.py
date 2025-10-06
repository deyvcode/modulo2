import requests

dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante')
result = dados.json()

for i in result:
     vav=i.get("Prato")
     print(vav)

if vav =="lasanha":
    # requests.delete('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{Prato}')
    print( 'foi')
else:
    print('qerh')

