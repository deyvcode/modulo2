import requests

# Prato = input()
# Bebida = input()
# Mesa = input()

rest = requests.get('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante')
print(rest.json())