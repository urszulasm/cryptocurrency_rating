from data_extraction import get_historical_data
from data_processing import data_preprocessing
from data_processing import merge_dfs

# Step 1 - BTC-USD and S&P 500 import
get_historical_data('BTC-USD')
get_historical_data('SPX')

# Step 2 - data preprocessing
btc = data_preprocessing('BTC-USD')
sp_500 = data_preprocessing('SPX')

# Step 3 - merging data frames
df_combined = merge_dfs([btc, sp_500])
