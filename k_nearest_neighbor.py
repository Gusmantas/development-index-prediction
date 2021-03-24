from sklearn.neighbors import KNeighborsClassifier
from data_processing import prepare_data
from operator import itemgetter
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

knn_classifier = KNeighborsClassifier(n_neighbors=4, metric='minkowski', p=2)

def train_knn_model():
    data = prepare_data()
    # Destructuring data for training
    X_train, y_train, = itemgetter('X_train', 'y_train',)(data)
    # Training KNN model
    knn_classifier.fit(X_train, y_train)
    print('KNN Trained OK')


def predict_knn(values):
    data = prepare_data()
    # Destructuring a dict with data to calculate model score
    X_test, y_test, standardScaler = itemgetter('X_test', 'y_test', 'standardScaler')(data)
    # Predicting results on test set
    knn_pred = knn_classifier.predict(X_test)

    knn_results = []
    # Accuracy score:
    knn_results.append(accuracy_score(y_test, knn_pred)) 

    # Creating an ndArray (2d array in numpy) so we can predict results
    values = np.array(values)
    # Reshapes array without modifying the data
    values = values.reshape(1, -1)
    knn_pred = knn_classifier.predict(standardScaler.transform(values)) 
    knn_results.append(knn_pred[0])
    return knn_results


# train_knn_model()
# # Population, population density, GDP, Literacy, Infant mortality in an array
# values = [86666, 166556322.9, 5000,	37.8,	1.7]
# print(predict_knn(values))
