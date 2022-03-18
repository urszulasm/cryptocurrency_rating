from data_extraction import get_historical_data
from data_processing import data_preprocessing
from data_processing import merge_dfs
from data_processing import calculate_pct_change
from data_processing import calculate_cumulative_return
from data_analysis import visualize_absolut_price

# Step 1 - BTC-USD and S&P 500 import
get_historical_data('BTC-USD')
get_historical_data('ETH-USD')
get_historical_data('SPX')

# Step 2 - data preprocessing
btc = data_preprocessing('BTC-USD')
eth = data_preprocessing('ETH-USD')
sp_500 = data_preprocessing('SPX')

# Step 3 - merging data frames
df_combined = merge_dfs([btc, eth])

# Step 4 - calculate daily returns
df_combined = calculate_pct_change(df_combined)

# Step 5 - calculate cumulative returns
df_combined = calculate_cumulative_return(df_combined)

