from typing import List

import numpy as np
import pandas as pd
from pandas import DataFrame
import re


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
    yf_df.rename(columns={'Close': f'{ticker}'}, inplace=True)

    return yf_df


def merge_dfs(list_of_dfs: List[DataFrame]) -> DataFrame:
    # dropping all columns except for closing value
    dfs_closing_value = [df.iloc[:, 3:4] for df in list_of_dfs]

    # merged DF with closing value column for each ticker
    df_combined = pd.concat(dfs_closing_value, join='outer', axis=1)

    # dropping NaN values
    return df_combined.dropna()


def calculate_pct_change(df: DataFrame) -> DataFrame:
    # get original df column names
    df_colum_names = df.columns
    df_copy = df.copy()

    # create new cols with % change based on previous day and return df w/o 1st row (with NaN values)
    for name in df_colum_names:
        df_copy[f'{name}_return_daily'] = df_copy[name].pct_change(1)  # 1 for ONE day look back

    # drop original columns
    df_copy.drop(df_colum_names, axis=1, inplace=True)

    return df_copy.iloc[1:, :]


def calculate_cumulative_return(df: DataFrame) -> DataFrame:

    pct_change_cols = df.columns
    df_copy = df.copy()

    # create new cols with calculated cumulative daily returns using cumprod func
    for name in pct_change_cols:
        df_copy[f'{name}_1'] = (1 + df_copy[name]).cumprod() - 1

    # replace 'daily_1' in col name with 'cumulative'
    df_copy.columns = [re.sub('daily_1', 'cumulative', c) for c in df_copy.columns]

    # drop original columns
    df_copy.drop(pct_change_cols, axis=1, inplace=True)

    return df_copy






