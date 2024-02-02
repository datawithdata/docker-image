# mlops
Cloud agnostic solution for deploying Machine Learning models in docker and kubernetes 
## Dockerfile
This file is used to build Docker Image where our inferencing logic and trained model is present

## predit.py
A simple python code that loads the trained model for the predictions based on the request

## app.py
REST API logic using Flask where our predict.py code is exposed as an API

## config.json
JSON file where user needs to provide details like Name of the deploying model and few other system configurations 
