import requests

while True:
    dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante').json()
    print(dados)

    op = int(input('Digite 1 para criar um pedido, digite 2 para deletar seu pedido ou digite 3 para atualizar seu pedido: '))

    if op == 1:
        prato=input('Digite o prato que você deseja: ')
        bebida=input('Digite a bebida de sua preferência: ')
        mesa=input('Digite a mesa a qual você deseja se sentar: ')
        pedido={
            'Prato': prato,
            'Bebida': bebida,
            'Mesa': mesa
        }
        requests.post('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante', pedido )
    elif op == 2:
        for i in dados:
            idd = i.get('id')
        id = int(input('Digite o item que você deseja deletar: '))
        requests.delete(f'https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{id}')