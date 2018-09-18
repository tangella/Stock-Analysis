import pandas as pd
import numpy as np
from iexfinance import get_historical_data
from datetime import datetime

# https://pypi.org/project/iexfinance/

IPOData = pd.read_excel("ipo.xlsx")
IPOData_np = np.array(IPOData)

def getQuote(index):
    print(IPOData_np[index,3])
    df = get_historical_data(IPOData_np[index,3], start=IPOData_np[index,8], end=IPOData_np[index,8] + timedelta(days=4), output_format="pandas")
    df_np = np.array(df)
    print(df_np[:,3])

