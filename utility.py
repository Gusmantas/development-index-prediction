def get_prediction_data(values):
  prediction_values = []
  for key, value in values.items():
    if key == "area":
      continue
    prediction_values.append(value)
  return prediction_values

def prepare_posting_data(values, prediction):
  data_to_post = []
  for value in values.values():
    data_to_post.append(value)
  data_to_post.append(str(prediction[1]))
  return data_to_post