import pandas as pd

dataframe = pd.read_csv(r"enderecos.csv", delimiter=";")
bairros = dataframe['BAIRRO'].unique()

for b in bairros:    
    filtrado = dataframe['BAIRRO'] == b
    end_por_bairro = dataframe[filtrado]
    end_por_bairro.to_excel("Bairros/"+b+".xlsx", index=False)
