let ctx = document.getElementById('myChart').getContext('2d');


let res = fetch('/rest/get-dataset').then(response => {
  return response.json()
}).then(data => {
  for(array in data){
    
  }
})

