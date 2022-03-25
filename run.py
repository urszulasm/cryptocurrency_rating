from data_extraction import get_historical_data
from data_processing import data_preprocessing, merge_dfs, calculate_pct_change, calculate_cumulative_return
from data_analysis import visualize_absolut_price, visualize_daily_returns, visualize_cumulative_returns, \
    visualize_cumulative_returns_checklist

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
# Step 4 - add calculated daily returns columns
df_combined_pct_change = calculate_pct_change(df_combined)

# Step 5 - add calculated cumulative daily returns columns
df_combined_cumulative = calculate_cumulative_return(df_combined_pct_change)

# Step 6 - visualize results
visualize_absolut_price(df_combined)
visualize_daily_returns(df_combined_pct_change)
visualize_cumulative_returns(df_combined_cumulative)
visualize_cumulative_returns_checklist(df_combined_cumulative)

a = 1
