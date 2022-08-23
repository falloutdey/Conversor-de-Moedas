# Bibliotecas
import requests as rq

# API
url = rq.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
url_json = url.json()
cotacao_dolar = float(url_json['USDBRL']['bid'])
cotacao_euro = float(url_json['EURBRL']['bid'])

# Programa

sentinela = 'SIM'
while sentinela == 'SIM':
    opcao = input('Para qual moeda você deseja converter?\n> ').upper()
    if opcao == 'DOLAR':
        real = float(input('Qual o valor em reais que será convertido?\n> '))
        valor = real / cotacao_dolar
        print(f'''
        O valor atual do Dolar é: US$ {cotacao_dolar:.2f}

        R$ {real} é igual a US$ {valor:.2f}
        ''')

    elif opcao == 'EURO':
        real = float(input('Qual o valor em reais que será convertido?\n> '))
        valor = real / cotacao_euro
        print(f'''
        O valor atual do Euro é: EUR {cotacao_euro:.2f}

        R$ {real:.0f} é igual a: EUR {valor:.2f}.
        ''')
    sentinela = input('Você deseja converter outro valor?\n> ').upper()
print('Programa finalizado! Foi um prazer te-lô aqui! :)')
