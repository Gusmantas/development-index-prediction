# development-index-prediction

A webservice built with python backend and Machine Learning connected to simple jQuery frontend.
* Tools used: 
* Sanic, 
* K-nearest-neighbor, 
* Random forest classifier, 
* jQuery, 
* chart.js

Reason for this app is to see two different predictions of two different ML models in UI, and to see how each line in database affects ML algorithms since every time a new prediction is saved both models are retrained. 

To run the app: 

* Open this folder with cmd (command-prompt in Mac)
* Run py `-m venv env` to create virtual environment
* Navigate to: `cd env` -> `cd scripts` -> `activate` to activatate “activate.bat” file (mac: cd env -> cd bin -> activate)
* Navate 2 steps back `cd ..`-> `cd ..`
* Run `py -m pip install sanic pandas sklearn`
* Run main.py file
* Open frontend with a url that runs in console.

Both models predict different development index results of an area, fictional or real. Every time all input fields are filled and predict button is hit, the data is saved in to the database with index taken from predictions (let us say that random forest has better accuracy score after it is retrained, therefore the index predicted by random forest is saved in the database together with all the other inputs and vice versa). 
