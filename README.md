# mlops
Cloud agnostic solution for deploying Machine Learning models in docker and kubernetes 
## Dockerfile
This file is used to build Docker Image where our inferencing logic and trained model is present

## predit.py
A simple python code that loads the trained model for the predictions based on the request

## app.py
REST API logic using Flask where our predict.py code is exposed as an API

## config.json

  - registry-name : Name of the model registry.  
  - model-version: Version of the model registered.
  - ecr-version: Docker Image version. This is used to deploy a model from Git Actions run use default in case if wanted to deploy a latest version.
  - ram: Memory needed to provide values in MB
  - CPU: CPU value provides the value from 0.1
  - deployment-type: use the keyword deploy to deploy the model after successful completion of Git Actions or use Build to build only docker Image
  - model_name: name of the trained ML model 
