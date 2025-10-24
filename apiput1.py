import requests

dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante').json()

for i in dados:
    id = i.get('id')
    print(id)

vaa = input('Escolha um ID: ')
prato = input('Escolha seu prato: ')
bebida = input('Escolha sua bebida: ')
mesa = input('Escolha sua mesa: ')
novopepe = {
    'Prato': prato,
    'Bebida': bebida,
    'Mesa': mesa
}
requests.put(f'https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{vaa}', novopepe)