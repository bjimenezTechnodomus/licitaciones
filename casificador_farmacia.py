#%% 
import pandas as pd
import gspread
import re

from pandas._config.config import describe_option

gc = gspread.service_account()
worksheet = gc.open('Total partidas').sheet1
rows = worksheet.get_all_records()
data = pd.DataFrame.from_records(rows)
data

#%%

descripciones = data[['Id_Partida', 'Descripción', 'Grupo de productos', 'Grupo Productos', 'Cuadro Básico']]
descripciones = descripciones['Descripción'].str.lower()

filtro1 = data[data['Descripción'].str.contains('farmacia hospitalaria en dosis unitarias')]
filtro2 = data[data['Descripción'].str.contains('abasto de medicamentos subrogado')]
# %%

dosis = data[data['Descripción'].str.contains('dosis medida')]