import requests

id=input('Digite o ID que vai ser deletado: ')
requests.delete(f'https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/{id}')
