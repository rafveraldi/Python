import pandas as pd

df = pd.read_csv('shortname.csv')

df = df.dropna(subset=['Noofwords'])

df['Noofwords'] = df['Noofwords'].astype('int')

df['ShortName'] = df.apply(lambda x: ' '.join(x['AccountName'].split(' ')[:x['Noofwords']]), axis=1)

df.to_csv('shortname2.csv')