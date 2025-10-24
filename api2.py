import requests

prato=input('Digite o prato que você deseja: ')
bebida=input('Digite a bebida que você deseja: ')
mesa=input('Digite a mesa a qual você deseja se sentar: ')

pedido={
    'Prato': prato,
    'Bebida': bebida,
    'Mesa': mesa
}
requests.post('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante', pedido )