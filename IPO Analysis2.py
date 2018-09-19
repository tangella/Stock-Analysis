import pandas as pd
import numpy as np
from iexfinance import get_historical_data
from datetime import datetime
from datetime import timedelta

# https://pypi.org/project/iexfinance/

IPOData = pd.read_excel("ipo.xlsx")
IPOData_np = np.array(IPOData)


def getQuote(index):
    print("processing " + IPOData_np[index,3] + "\n")
    try:
        df = get_historical_data(IPOData_np[index,3], 
                                 start=IPOData_np[index,1] + timedelta(days=31), 
                                 end=IPOData_np[index,1] + timedelta(days=35), 
                                 output_format="pandas")
        print(df.loc[df.index[0], 'close'])
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'One Month'] = IPOData_np[index,1] + timedelta(days=31)
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'Price Date'] = df.index[0]
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'Current Price'] = df.loc[df.index[0], 'close']
        
    except:
        # update the original price as target price and also original date as 
        # one Month and Price Date
        print("Symbol Not found and updating the current price to original\n")
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'One Month'] = IPOData_np[index,1]
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'Price Date'] = IPOData_np[index,1]
        IPOData.loc[IPOData['Symbol'] == IPOData_np[index,3], 
                    'Current Price'] = IPOData_np[index,2]

# complete the processing
for i in range(0,np.size(IPOData_np,0)):
    getQuote(i)

writer = pd.ExcelWriter('ipoOut.xlsx')
IPOData.to_excel(writer,'Sheet1')
writer.save()