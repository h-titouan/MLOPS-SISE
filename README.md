# MLOPS-SISE
Build a server and client application for a Machine Learning model

## Purpose of the repository

This repository present a web application made with Streamlit which is connected to an API to get a prediction based on Iris Dataset.

You have to set the parameters of your future prediction with the sliders. 
It will return the class of the iris and display an image of which iris you predict.

## How to use this repository

### Mandatory
If you want to try it, you have to :

* Get Docker Desktop and run it

### Setup 

```
$ cd 'path/to/repository/folder'
$ docker compose up --build
```

### Run application and API

Once the previous steps have been completed, launch these links in a browser : 

localhost:8501 for the Streamlit Application
localhost:8000 for the API
