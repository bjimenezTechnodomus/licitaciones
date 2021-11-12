#%%
import gspread

import pandas as pd
import re

gc = gspread.service_account()
# %%
worksheet = gc.open('Total partidas').sheet1

rows = worksheet.get_all_values()

data = pd.DataFrame.from_records(rows)
data.columns = data.iloc[0]
data.drop(0, inplace=True)
display(data.info())
display(data.describe())

#%%
