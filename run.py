from data_extraction import get_historical_data
from data_processing import data_preprocessing

# Step 1 - BTC-USD and S&P 500 import
get_historical_data('BTC-USD')
get_historical_data('SPX')

# Step 2 - data preprocessing
btc = data_preprocessing('BTC-USD')
sp_500 = data_preprocessing('SPX')
