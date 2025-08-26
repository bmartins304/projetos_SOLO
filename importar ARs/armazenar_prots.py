import pandas as pd


class criar_dataFrame:

    def __init__(self,protocolos):
        self.lista_protocolos = protocolos
    
    def dataframe(self):
        dataframe = pd.DataFrame({'protocolos': self.lista_protocolos})
        dataframe.to_csv('protocolos',sep=";")
        print(dataframe)
        
    def acessando_datafrema():
        pass