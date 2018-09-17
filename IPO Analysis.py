import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as fyf
from pandas_datareader import data as pdr
import numpy as np
import datetime
import xlrd
fyf.pdr_override()
# We will look at stock prices over the past year, starting at January 1, 2016
#startd = datetime.datetime(2016,1,1)
#endd = datetime.date.today()
 
#BABA = pdr.get_data_yahoo("BABA", start=startd, end=endd)
#BABA = pdr.get_data_yahoo("BABA", start=endd, end=endd)
#BABA_np = np.array(BABA)

#type(BABA)
#print(BABA_np)
df = pd.read_excel("ipo.xlsx")

print(df.columns)
