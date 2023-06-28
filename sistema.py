import requests
import json

def menu():
    print('Olá, seja bem-vindo!')
    cep = input("Qual o CEP? ")
    link = f'https://cep.awesomeapi.com.br/json/{cep}'

    requisicao = requests.get(link)
    dados = requisicao.json()

    if "error" in dados:
        print("CEP não encontrado. Por favor, verifique o CEP e tente novamente.")
        return

    print("Endereço:")
    print(f"CEP: {dados['cep']}")
    print(f"Tipo de Endereço: {dados['address_type']}")
    print(f"Nome do Endereço: {dados['address_name']}")
    print(f"Endereço: {dados['address']}")
    print(f"Estado: {dados['state']}")
    print(f"Bairro: {dados['district']}")
    print(f"Latitude: {dados['lat']}")
    print(f"Longitude: {dados['lng']}")
    print(f"Cidade: {dados['city']}")
    print(f"Código IBGE da Cidade: {dados['city_ibge']}")
    print(f"DDD: {dados['ddd']}")

while True:
    menu()
