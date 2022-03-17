import yfinance as yf


# function to get historical data for specified tickers
def get_historical_data(ticker: str):

    yf_object = yf.Ticker(ticker)

    yf_historical = yf_object.history(period='max')

    # save data to csv file
    yf_historical.to_csv(f'{ticker}_historic_data.csv')
