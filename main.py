#========================================================
# cordeirolibel and daviboberg - 2017
# https://github.com/cordeirolibel/Titanic/
#========================================================

import pandas as pd
import numpy as np

# same items with same number
def enumerate(data,col):
	# Get the unique values in the column
	values = list(set(data[col]))  

	k=1
	for v in values:
		data[col] = data[col].replace(v,k)
		k+=1
	
	return data



def adjust(data):

	data_y = data['Survived']

	# Organize
	data = enumerate(data,'Sex')
	data = enumerate(data,'Embarked')
	data = enumerate(data,'Ticket')
	# to do: 'Cabin'

	# Create new cols
	data['name_count'] = data['Name'].str.split().str.len()

	#Remove
	remove = ['PassengerId','Survived','Name']
	data = data.drop(remove, 1)

	# to do: Normalize

	return data, data_y



#   Dataframes
df_train = pd.read_csv('data/train.csv')
df_test = pd.read_csv('data/test.csv')

df_train,df_y = adjust(df_train)

print(df_train.head())
