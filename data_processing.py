import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3
from utility import prepare_posting_data

con = sqlite3.connect("development-index.db")
current = con.cursor()

def prepare_data():
  df = pd.read_sql_query('SELECT * FROM developmentIndex', con)

  # print(df.head())
  # print(df.shape)

  # Checking if there are null values
  # print(df.isnull().sum())

  # Removing area column since we don't need it

  df.drop(labels=['Area'], axis=1, inplace=True)

  # print(df.head())
  
  # Splitting into dependent/independent variables
  X = df.iloc[:, :-1].values
  y = df.iloc[:, -1].values

  # Splitting into train/test sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

  # Feature scaling
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.fit_transform(X_test)

  # Returning all values so we can train model elswhere, as well as
  # returning standardScaler since it is fitted and ready to be applied on new values
  data = {"X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test, "standardScaler": sc}
  return data

def getDataset():
  current.execute('SELECT * FROM developmentIndex')
  rows = current.fetchall()

  dicts = []
  for row in rows:
    dicts.append(row)
  return dicts

def savePrediction(values, predictedIndex):
  dataArray = prepare_posting_data(values, predictedIndex)
  print(dataArray)
  query = '''INSERT INTO developmentIndex(Population, Area, Pop_density, GDP, Literacy, Infant_mortality, Development_index) 
            VALUES(?, ?, ?, ?, ?, ?, ?)'''
  current.execute(query, dataArray)
  con.commit()

