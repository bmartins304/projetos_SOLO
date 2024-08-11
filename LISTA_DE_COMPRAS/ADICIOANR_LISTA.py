import molde
from time import sleep
import os
from datetime import date


def adicionar():
    molde.molde_adicionar()
    
    while True:
        
        NOME = str(input('NOME DO PRODUTO: ')).upper()
        while True:
            try:
                PRECO = float(input('PREÇO DO PRODUTO: '))
            except ValueError:
                print('Por favor! Informar o valor correto do produto')
            else:
                break

        with open('lista_compras.txt','a') as arquivo: # Adicionar o nome e o preco no arquivo de texto
            arquivo.write(f'NOME: {NOME}-PRECO: {PRECO:.2f};')

        key = int(input('[1] continuar ou [999] para parar:')) # continuar preenchendo
               
        if key == 999:
            break
 
    pontinhos = ('.','.','.')
    print('Adicionando',end='')
    for i in pontinhos:
        print(i,flush=True,end='')
        sleep(1) 
    sleep(1)
    os.system('cls') or None
    print('PRODUTO ADICIONADO NA LISTA')
    sleep(0.5)
    
