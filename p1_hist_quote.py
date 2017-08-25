import datetime as dt
import matplotlib.pyplot as plt
#from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#style.use('ggplot')
start = dt.datetime(2000, 1, 1)
end = dt.datetime(2017, 8, 1)


df = web.DataReader('COF', 'yahoo', start, end)
print (df.tail(6))
print(df[['Open', 'High']].head())

df['Adj Close'].plot(title='Capital One')
plt.show()