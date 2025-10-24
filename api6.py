import requests

dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante').json()


for i in dados:
    mesa=i.get("Mesa")
    id=i.get("id")
    prato=i.get("Prato")
    bebida=i.get("Bebida")
    print(mesa)

    if id=='5':
        pedido={
         'Prato': prato,
         'Bebida': bebida,
         'Mesa': '6'
        }
        requests.post('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante', pedido)
        requests.delete(f'https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{id}')