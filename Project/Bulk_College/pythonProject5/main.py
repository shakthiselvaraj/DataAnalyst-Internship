import pandas as pd
import numpy as np
a = pd.read_csv("C:\\Users\\shakt\\Downloads\\College Data to clean and sort.xlsx - Bulk College Data.csv")
a.head()

print(a.shape)
a.describe()
print(a.isnull().sum().sort_values(ascending=False))