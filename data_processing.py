from typing import List

import pandas as pd
from pandas import DataFrame


def data_preprocessing(ticker: str) -> DataFrame:

    # data import
    yf_df = pd.read_csv(f'{ticker}_historic_data.csv')

    # rounding numeric values to 2 decimals
    yf_df = yf_df.round(2)

    # check for null values
    print(yf_df.isnull().sum())
    yf_df.dropna(inplace=True)

    # converting the Date column to datetime type
    yf_df['Date'] = pd.to_datetime(yf_df['Date'])

    # setting Date column as df index and dropping Date column
    yf_df.index = yf_df['Date']
    yf_df.drop('Date', axis=1, inplace=True)

    # renaming Close column to add ticker name
    yf_df.rename(columns={'Close': f'Close {ticker}'}, inplace=True)

    return yf_df


def merge_dfs(list_of_dfs: List[DataFrame]) -> DataFrame:
    # dropping all columns except for closing value
    dfs_closing_value = [df.iloc[:, 3:4] for df in list_of_dfs]

    # merged DF with closing value column for each ticker
    df_combined = pd.concat(dfs_closing_value, join='outer', axis=1)

    # dropping NaN values
    return df_combined.dropna(inplace=True)