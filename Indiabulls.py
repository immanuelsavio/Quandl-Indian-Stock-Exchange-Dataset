import pandas as pandas
import quandl

data = quandl.get("NSE/IBULISL")
data = data[['Open','High', 'Low', 'Last', 'Close']]

data['Avrg'] = (data['High'] + data['Low']) / 2

data = data[['High', 'Low', 'Avrg']]

print(data.head)

