import pandas as pd

# Ruta al archivo
archivo = "Corrientes/A872914.xls"

# Leer el archivo Excel
df = pd.read_excel(archivo)

for col in df.columns:
    print(col)

