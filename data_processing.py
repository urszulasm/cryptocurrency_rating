import pandas as pd
from pandas import DataFrame


def data_preprocessing(ticker: str) -> DataFrame:

    # data import
    yf_df = pd.read_csv(f'{ticker}_historic_data.csv')

    # rounding numeric values to 2 decimals
    yf_df = yf_df.round(2)

    # check for null values
    print(yf_df.isnull().sum())

    # converting the Date column to datetime type
    yf_df['Date'] = pd.to_datetime(yf_df['Date'])

    # setting Date column as df index and dropping Date column
    yf_df.index = yf_df['Date']
    yf_df.drop('Date', axis=1, inplace=True)

    return yf_df
