from enum import unique
import pandas as pd

csv_path='file.csv'

df= pd.read_csv(csv_path)

df.head()

#we can convert a dictionary into a dataframe
    
df[release].unique


x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df.to_clipboard()