import arquivo
import func_lista
from datetime import date
import molde

def fazer_relatorio():
    resumo = dict()
    preco= list()

    data = [date.today().day,date.today().month,date.today().year]

    lista_contagem = func_lista.lista()

    func_lista.mostrar_visu()

    soma_preco = 0
    maior_preco = 0
    indice = 0


    for item in lista_contagem:
        preco.append(item[1].split(':'))
        
    for i,item_do in enumerate(preco):
        quardar_preco = float(item_do[1])
        soma_preco += quardar_preco
        if quardar_preco > maior_preco:
            maior_preco = quardar_preco
            indice = i

    item_mais_caro = lista_contagem[indice][0].split(':')
 
    contagem_itens = len(lista_contagem)
      
    print(f'Relatorio criado na data:              {str(data)}')
    molde.traco()
    print(f'A quantidade de itens dentro da lista: {contagem_itens}')
    molde.traco()
    print(f'Valor total da compra:                 {soma_preco}')
    molde.traco()
    print(f'O item mais caro:                      {str(item_mais_caro[1])}')
        

        
    
  
    

    
    