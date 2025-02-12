#!/usr/bin/env python3

#import the package "Pandas" into Jupyter Notebook
import pandas as pd

#We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace
#We then name the DataFrame name as 'fb'
# Note: the actual data is only found in the Coursera-lined Notebook lab
# Note: You need to tell which column of the csv file you want to set as index,
# for example, the first column with "index_col=0".
# Otherwise, it will use 0,1,2,3..as index by default. 		
fb = pd.read_csv('../data/facebook.csv', index_col=0)
ms = pd.read_csv('../data/microsoft.csv', index_col=0)

# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])
# Expected output is 46.73
# Note: The iloc function is a function found in the Pandas module. 
# It is a powerful tool that enables users to select specific rows and columns of a DataFrame by their integer position. 
# It can extract a subset of a DataFrame, 
# perform conditional indexing, 
# or assign values to particular rows and columns.