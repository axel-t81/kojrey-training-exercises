# Add this to the top of all files
#!/usr/bin/env python3

from IPython.display import display
# Import pandas and use abbreviation
import pandas as pd

# Use read_csv to import the data from CSV
btc = pd.read_csv('bitcoin_historical_data-4-b.csv', index_col=0)


# Run this to test data has imported correctly
print(btc.iloc[0:,7])
