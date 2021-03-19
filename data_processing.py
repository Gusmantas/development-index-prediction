import pandas as pd 

def prepare_data():
  df = pd.read_csv('development-index.csv')

  # print(df.head())
  # print(df.shape)

  # Checking if there are null values
  # print(df.isnull().sum())

  # Removing area column since we don't need it

  df.drop(labels=['Area'], axis=1, inplace=True)

  # print(df.head())
  
  X = df.iloc[:, :-1].values
  y = df.iloc[:, -1].values

  print(X)
  print(type(X))
  print(y)

prepare_data()
