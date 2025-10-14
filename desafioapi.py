import requests

while True:
    dados = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante').json()

    op = int(input('Digite 1 para criar um pedido\n digite 2 para deletar seu pedido\n digite 3 para atualizar seu pedido\n digite 4 para ver todos os pedidos: '))

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
    elif op == 3:
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
    elif op == 4:
        for item in dados:
          print('pedido:',item.get('Prato'),item.get('Bebida'))
          print()
