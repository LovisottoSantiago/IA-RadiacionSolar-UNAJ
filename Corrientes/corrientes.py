# Borrar Columna con datos nulos, borró temp interperie 5cm minima, temp interperie 50cm minima, 
# temp suelo 5cm media, temp inte 5cm, temp interperie 150cm min, humedad suelo.

import pandas as pd
import matplotlib.pyplot as plt
import xlrd

# Cargamos Corriente - Lovi
urlSF1="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872914.xls"
urlSF2="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872915.xls"
urlSF3="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872916.xls"
urlSF4="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872950.xls"
urlSF5="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872951.xls"
urlSF6="https://raw.githubusercontent.com/LovisottoSantiago/IA-RadiacionSolar-UNAJ/main/Corrientes/A872952.xls"

# Guardamos el dataframe
dfSF1 = pd.read_excel(urlSF1, engine="xlrd")
dfSF2 = pd.read_excel(urlSF2, engine ="xlrd")
dfSF3 = pd.read_excel(urlSF3, engine ="xlrd")
dfSF4 = pd.read_excel(urlSF4, engine ="xlrd")
dfSF5 = pd.read_excel(urlSF5, engine ="xlrd")   
dfSF6 = pd.read_excel(urlSF6, engine ="xlrd")   


# Lista de los dataframes
lista_data = [dfSF1, dfSF2, dfSF3, dfSF4, dfSF5, dfSF6]

lista_data.info()



