import pandas as pd

df = pd.read_csv('shortname.csv')

df['Noofwords'] = df['Noofwords'].fillna(0) # Fill NaN with 0

df['Noofwords'] = df['Noofwords'].astype('int') # Tranform from float to int

print(df['Noofwords'].unique()) # Unique values are [1 2 0]

df = df.sort_values(by=['Noofwords']).reset_index() # Reset index after sorting ascending

print(df.Noofwords.values.searchsorted('1', side='left')) # Search first index for value 1: index 44 
print(df.Noofwords.values.searchsorted('2', side='left')) # Search first index for value 2: index 164

# Slicing into 3 different dataframes 
df1 = df[:44] 
df2 = df[44:164]
df3 = df[164:]

# Populating 'Short Name' column
df1['ShortName'] = None
df2['ShortName'] = df2['AccountName'].str.split().str[:1].str.join(" ").str.replace(",","") # Split, slice and join into a string
df3['ShortName'] = df3['AccountName'].str.split().str[:2].str.join(" ").str.replace(",","") # Split, slice and join into a string

df = pd.concat([df1,df2,df3]) # Concatenate the different dataframes back to the original 

df.to_csv('shortname2.csv', columns=['AccountID','AccountName','Noofwords','ShortName'])


