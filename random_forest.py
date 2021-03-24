from data_processing import prepare_data
from operator import itemgetter
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

rf_classifier = RandomForestClassifier(
    n_estimators=10, criterion='entropy', random_state=0)

# Training model
def train_random_forest():
    # Data comes from data_preprocessing.py
    data = prepare_data()
    # Destructuring data required for training
    X_train, y_train = itemgetter('X_train', 'y_train')(data)

    rf_classifier.fit(X_train, y_train)
    print('Random Forest Trained OK')


def predict_random_forest(values):
    data = prepare_data()
    # Destructuring data for accuracy calculations/prediction
    X_test, y_test, standardScaler = itemgetter('X_test', 'y_test', 'standardScaler')(data)
     # testing model on test results
    rf_predict = rf_classifier.predict(X_test)

    rf_results = []
    # Getting accuracy score in percentage
    rf_results.append(accuracy_score(y_test, rf_predict))

    # Creating an ndArray (2d array in numpy) so we can predict results
    values = np.array(values)
    # Reshapes array without modifying the data
    values = values.reshape(1, -1)
    # Predicting new results
    rf_predict = rf_classifier.predict(standardScaler.transform(values))
    rf_results.append(rf_predict[0])
    return rf_results


# train_random_forest()
# Population, population density, GDP, Literacy, Infant mortality in an array
# values = [5450661, 126.5,	31100, 100, 4.56]
# print('prediction')
# print(predict_random_forest(values))
