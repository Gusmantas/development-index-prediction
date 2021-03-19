import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3

con = sqlite3.connect("development-index.db")

def prepare_data():
  df = pd.read_sql_query('SELECT * FROM developmentIndex', con)

  # print(df.head())
  # print(df.shape)

  # Checking if there are null values
  # print(df.isnull().sum())

  # Removing area column since we don't need it

  df.drop(labels=['Area\n'], axis=1, inplace=True)

  # print(df.head())
  
  # Splitting into dependent/independent variables
  X = df.iloc[:, :-1].values
  y = df.iloc[:, -1].values

  # print(X)
  # print(type(X))
  # print(y)

  # Splitting into train/test sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  # print(X_train)
  # print(X_test)
  # print(y_train)
  # print(y_test)

  # Feature scaling
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.fit_transform(X_test)

  # Returning all values so we can train model elswhere, as well as
  # returning standardScaler since it is fitted and ready to be applied on new values
  data = {"X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test, "standardScaler": sc}
  # con.close()
  return data

def getDataset():
  current = con.cursor()
  current.execute('SELECT * FROM developmentIndex')

  rows = current.fetchall()
  # con.close()
  dicts = []
  for row in rows:
    dicts.append(row)
  return rows

