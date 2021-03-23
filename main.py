from sanic import Sanic, response as res
from sanic.exceptions import NotFound
from k_nearest_neighbor import train_knn_model, predict_knn 
from random_forest import train_random_forest, predict_random_forest 

app = Sanic(__name__)
train_random_forest()
train_knn_model()


@app.post('api/predict')
async def predict_results(req):
  values = []
  temp_values = req.json
  for value in temp_values.values():
    values.append(value)
  
  knn_prediction = predict_knn(values)
  random_forest_prediction = predict_random_forest(values)

  results = {"knn": int(knn_prediction[0]), "random-forest": int(random_forest_prediction[0])}
  return res.json(results)


@app.get('rest/get-dataset')
async def get_dataset(req):
  from data_processing import getDataset
  dataset = getDataset()
  # print(dataset)
  return res.json(dataset)

# When we navigate to '/' - serve the dist folder
app.static('/', './dist')

@app.exception(NotFound)
async def ignore_404s(req, err):
  return await res.file('./dist/index.html')

if __name__ == "__main__":
  app.run(port=8000) 