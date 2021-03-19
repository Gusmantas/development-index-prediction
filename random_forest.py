from data_processing import prepare_data
from operator import itemgetter
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

rf_classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
data = prepare_data()
# Destructuring a dict with data from data_processing.py
X_train, X_test, y_train, y_test, standardScaler = itemgetter('X_train', 'X_test', 'y_train', 'y_test', 'standardScaler')(data)

# Training model
def train_random_forest():
  rf_classifier.fit(X_train, y_train)

  # Predict test results with 
  # print(type(X_test))
  rf_predict = rf_classifier.predict(X_test)

  # Creating a confusion matrix of prediction and actual results
  # cm = confusion_matrix(y_test, rf_predict)
  # Displaying accuracy score in percentage
  # print(accuracy_score(y_test, rf_predict))

def predict_random_forest(values):
  # Creating an ndArray (2d array in numpy) so we can predict results
  values = np.array(values)
  # Reshapes array without modifying the data
  values = values.reshape(1, -1)
  
  rf_predict = rf_classifier.predict(standardScaler.transform(values))
  return rf_predict

train_random_forest()

# Population, population density, GDP, Literacy, Infant mortality in an array
values = [5450661, 126.5,	31100, 100, 4.56]
print('prediction')
print(predict_random_forest(values))
