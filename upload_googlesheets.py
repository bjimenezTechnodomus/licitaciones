#%%
import gspread 
import pandas as pd
import time

gc = gspread.service_account()
batch_size = 20000
last_row = 1669000
limit = 2594899
row_n = 420002

for i in range(last_row, limit, batch_size):
    sh = gc.open('Datos para bajar_2').sheet1
    sh.add_rows(batch_size)
    data = pd.read_csv('partidas_solicitante2.csv', skiprows=i, nrows=batch_size)

    ids = data.iloc[:,0]
    convoc = data.iloc[:,1]
    descri = data.iloc[:,2]

    ids = list(map(lambda x: [x], ids))
    convoc = list(map(lambda x: [x], convoc))
    descri = list(map(lambda x: [x], descri))
    print(sh.row_count)
    print(row_n)
    while sh.row_count < row_n:
        sh = gc.open('Datos para bajar_2').sheet1
        sh.add_rows(1)
        time.sleep(2)
        print(sh.row_count)

    row = str(row_n)
    sh.batch_update([{'range': 'A'+row, 'values':ids}, {'range': 'B'+row, 'values':convoc}, {'range': 'C'+row, 'values':descri}])
    row_n = row_n + batch_size
    print(f'Ultima celda {row_n + batch_size}')
    print(f'Ultima fila archivo {last_row + batch_size}')
# %%
