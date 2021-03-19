from sklearn.neighbors import KNeighborsClassifier
from data_processing import prepare_data
from operator import itemgetter
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np


# getting data from data_processing.py
data = prepare_data()

# Destructuring a dict with data from data_processing.py
X_train, X_test, y_train, y_test, standardScaler = itemgetter(
    'X_train', 'X_test', 'y_train', 'y_test', 'standardScaler')(data)

knn_classifier = KNeighborsClassifier(n_neighbors=4, metric='minkowski', p=2)
print('KNN Trained OK')

def train_knn_model():
    # Training KNN model
    knn_classifier.fit(X_train, y_train)

    # Predicting results on test set
    # knn_pred = knn_classifier.predict(X_test)

    # Accuracy score:
    # print(confusion_matrix(y_test, knn_pred))
    # print(accuracy_score(y_test, knn_pred))


def predict_knn(values):
    # Creating an ndArray (2d array in numpy) so we can predict results
    values = np.array(values)
    # Reshapes array without modifying the data
    values = values.reshape(1, -1)
    knn_pred = knn_classifier.predict(standardScaler.transform(values))
    return knn_pred


# train_knn_model()
# # Population, population density, GDP, Literacy, Infant mortality in an array
# values = [8863338, 13.9, 500,	37.8,	116.7]
# print(predict_knn(values))
