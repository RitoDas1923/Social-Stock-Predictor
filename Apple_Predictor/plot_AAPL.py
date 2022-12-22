import pandas as pd
import pickle
import matplotlib.pyplot as plt
import base64
from io import BytesIO


from pandas import date_range

def plot(stockname, start_date, end_date):
    # Plot predicted values and date
    df = pd.read_csv('merged_' + stockname  + '.csv')
    df['Dates'] = pd.to_datetime(df['Dates'])
    df = df.set_index('Dates')
    # Create a new column with the predicted values
    xgbr = pickle.load(open('Bestmodel_' + stockname + '.sav', 'rb'))
    df['Predicted'] = xgbr.predict(df['Sentiment'].values.reshape(-1, 1))
    # Remove duplicate dates
    df = df[~df.index.duplicated(keep='last')]
    # Plot the graph of the stock price and the predicted values
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    mask = (df.index > start_date) & (df.index <= end_date)
    df = df.loc[mask]
    df['Predicted'].plot(figsize=(16, 6))
    plt.title('Predicted Price (Blue) vs Actual Price(Red) ' + stockname)
    plt.ylabel('Price')
    df['Close'].plot(figsize=(16, 6))
    plt.xlabel('Date')
    plt.savefig('./static/plot.jpg')

if __name__ == '__main__':
    plot('AAPL', '2022-09-10', '2022-09-17')