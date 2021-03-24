from sanic import Sanic, response as res
from sanic.exceptions import NotFound
from k_nearest_neighbor import train_knn_model, predict_knn
from random_forest import train_random_forest, predict_random_forest
from data_processing import getDataset, savePrediction
from utility import get_prediction_data


app = Sanic(__name__)
train_random_forest()
train_knn_model()


@app.post('api/predict')
async def predict_results(req):
    values = req.json
    prediction_values = get_prediction_data(values)


    knn_prediction = predict_knn(prediction_values)
    random_forest_prediction = predict_random_forest(prediction_values)

    print('knn', knn_prediction[0])

    savePrediction(values, random_forest_prediction)
    train_knn_model()
    train_random_forest()

    results = {"knn": int(knn_prediction[1]), "knn-score": knn_prediction[0], "random-forest": int(random_forest_prediction[1]), "rf-score": random_forest_prediction[0]}
    return res.json(results)


@app.get('rest/get-dataset')
async def get_dataset(req):
    dataset = getDataset()
    return res.json(dataset)

app.static('/', './dist')


@app.exception(NotFound)
async def ignore_404s(req, err):
    return await res.file('./dist/index.html')

if __name__ == "__main__":
    app.run(port=8000)
