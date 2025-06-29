#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas library used for data manipulation and analytics, great for structured data such as dfs
import pandas as pd 


# DF-DataFrame(tabular data structure) PD-pandas 
#csv(Comma Separated Values) - file format that stores tabular data separated by commas 
df = pd.read_csv("/Users/briannacarlisle/Downloads/employees_1000.csv")

#displays first few lines of content in csv 
print(df)







