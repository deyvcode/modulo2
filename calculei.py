import streamlit as sd

sd.sidebar.image('cal.png')
sd.sidebar.title('Calculadora')

num = sd.text_input('Digite um número: ')
num2 = sd.text_input('Digite outro número: ')

num1 = sd.text_input('Digite qulquer número: ')
num3 = sd.text_input('Digite de novo número: ')

num4 = sd.text_input('Digite mais um número: ')
num5 = sd.text_input('Digite outra vez: ')

num0 = sd.text_input('Escolha um número: ')
num6 = sd.text_input('Escolha outro número: ')

colunas = sd.columns(4)

with colunas[0]:
    botao0 = sd.button('SOMA')


    sd.title('coluna 1')

    if botao == True:
        num = float(num)
        num2 = float(num2)
        resposta = num + num2
        sd.write(resposta)

with colunas[1]:
    botao1 = sd.button('SUBTRAÇÃO')


    sd.title('coluna 2 ')

    if botao == True:
     num1 = float(num1)
     num3 = float(num3)
     resposta1 = num1 - num3
     sd.write(resposta1)

with colunas[2]:
    botao2 = sd.button('DIVISÃO')

    

    sd.title('coluna 3 ')

    if botao == True:
     num4 = float(num4)
     num5 = float(num5)
     resposta2 = num4 / num5
     sd.write(resposta2)

with colunas[3]:
    botao3 = sd.button('MÚLTIPLICAÇÃO')

    sd.title('coluna 4 ')

    if botao == True:
     num0 = float(num0)
     num6 = float(num6)
     resposta3 = num0 * num6
     sd.write(resposta3)