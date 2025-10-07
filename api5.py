import requests

dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante')
result = dados.json()

for i in result:
    id = i.get('id')
    vav=i.get("Prato")
    print(vav)

    if 'lasanha' in vav:
        requests.delete(f'https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{id}')
    else:
        print('Este item não será deletado pois não existe')

