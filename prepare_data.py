

"""Prepare the data"""

#!/usr/bin/env python
#chmod +x prepare.py
import pandas as pd

train_df = pd.read_csv('ice_train.tsv', sep='\t', header=None)
train_df = train_df.rename(columns={0: "Orthography", 1: "Phonetic"})
#adding spaces in column 1
train_df['Orthography'] = train_df['Orthography'].replace(to_replace=r'(.)', value=r' \1', regex=True)
# print(train_df)

ortho_list = train_df['Orthography'].to_list()

phono_list = train_df['Phonetic'].to_list()

with open(r'train.ice.p', 'w') as out:
    for item in phono_list:
        out.write(item + '\n')

with open(r'train.ice.g', 'w') as out:
    for item in ortho_list:
        out.write(item + '\n')
        
df1 = pd.read_csv('ice_dev.tsv', sep='\t', header=None)
df1 = df1.rename(columns={0: "Orthography", 1: "Phonetic"})
df1['Orthography'] = df1['Orthography'].replace(to_replace=r'(.)', value=r' \1', regex=True)
# print(df1)

ortho_list = df1['Orthography'].to_list()
        
phono_list = df1['Phonetic'].to_list()

with open(r'dev.ice.g', 'w') as out:
    for item in ortho_list:
        out.write(item + '\n')

with open(r'dev.ice.p', 'w') as out:
    for item in phono_list:
        out.write(item + '\n')
        
df3 = pd.read_csv('ice_test.tsv', sep='\t')
df3 = df3.rename(columns={"alls": "Orthography", "a l s": "Phonetic"})
df3['Orthography'] = df3['Orthography'].replace(to_replace=r'(.)', value=r' \1', regex=True)
# print(df3)

ortho_list = df3['Orthography'].to_list()

phono_list = df3['Phonetic'].to_list()

with open(r'test.ice.g', 'w') as out:
    for item in ortho_list:
        out.write(item + '\n')

with open(r'test.ice.p', 'w') as out:
    for item in phono_list:
        out.write(item + '\n')


