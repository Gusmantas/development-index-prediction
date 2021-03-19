from sanic import Sanic, response
from k_nearest_neighbor import train_knn_model, predict_knn 
from random_forest import train_random_forest, predict_random_forest 

app = Sanic(__name__)
train_random_forest()
train_knn_model()


@app.post('api/predict')
def prediction_results(req):
  values = []
  temp_values = req.json
  for value in temp_values.values():
    values.append(value)
  
  knn_prediction = predict_knn(values)
  random_forest_prediction = predict_random_forest(values)

  print('Knn Prediction:', knn_prediction)
  print('Random Forest Prediction:', random_forest_prediction)
  results = {"knn": int(knn_prediction[0]), "random-forest": int(random_forest_prediction[0])}
  return response.json(results)


if __name__ == "__main__":
  app.run(port=8000) 