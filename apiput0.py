import requests

novoped = {
    'Prato':'lasanha',
    'Bebida':'pepsi',
    'Mesa':'8'
}
requests.put('https://68dd8c16d7b591b4b78cc26a.mockapi.io/Restaurante/8', novoped)