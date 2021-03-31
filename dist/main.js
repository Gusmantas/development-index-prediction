let ctx = document.getElementById('myChart').getContext('2d');

function getDataset(){
  let res = fetch('/rest/get-dataset')
    .then(response => {
      return response.json()
    })
    .then(data => {
      let pieData = calculateData(data)
      createChart(pieData)
    })
}

getDataset()


function calculateData(data) {
  let devIndexes = []
  data.forEach(el => devIndexes.push(el[6]))

  let index1 = 0
  let index2 = 0
  let index3 = 0
  let index4 = 0

  devIndexes.forEach(el => {
    if (el === 1) {
      index1++
    } else if (el === 2) {
      index2++
    } else if (el === 3) {
      index3++
    } else {
      index4++
    }
  })
  devIndexes.splice(0, devIndexes.length)
  devIndexes = [index1, index2, index3, index4]

  return devIndexes
}

function createChart(pieData) {
  var chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Development index 1', 'Development index 2', 'Development index 3', 'Development index 4',],
      datasets: [{
        label: 'Development Index Statistics:',
        data: pieData,
        backgroundColor: [
          'rgba(255, 99, 133, 0.74)',
          'rgba(54, 163, 235, 0.74)',
          'rgba(255, 206, 86, 0.74)',
          'rgba(75, 192, 192, 0.74)',
        ],
        options: {
          events: ['click']
        }
      }]
    },
  });
}

$('#predict-form').submit(async function (e) {
  e.preventDefault()
  let inputs = $('#predict-form :input');

  let values = {};
  inputs.each(function () {
    if($(this).val())
    values[this.id] = $(this).val()
  });
  let res = await fetch('/api/predict', {
    method: 'POST',
    body: JSON.stringify(values)
  })

  let prediction = await res.json()
  console.log(prediction)
  
  $('#prediction').html(`
    K-Nearest-Neighbor prediction: <em>${prediction['knn']}</em>
    <br>
    Random-Forest prediction: <em>${prediction['random-forest']}</em> <br>
    Note! <br>
    KNN accuracy score: <em>${parseFloat(prediction['knn-score'] * 100).toFixed(1)}%</em> <br>
    Random Forest accuracy score: <em>${parseFloat(prediction['rf-score'] * 100).toFixed(1)}%</em> 
  `)

  getDataset()
})
