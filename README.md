# python-api
This is a simple python api meant to be deployed in docker, and then k8s.


## Architecture
This is a python application built into a Docker container. 

The python api is built using flask, and will run on port 5000.

The container will be deployed on k8s (into GKE as of 20-Oct-2020)
The loadbalancer will be on an external ip address listening on port 8080. 
To see the api you can `curl http:<external-ip>:8080/api/v1/message/`

The external ip can be found in the output of the app deployment in the google action

For now, the initial setup of GKE is to be done manually in the GCloud console.

Everything will be automatically built, deployed, and tested via a GitHub action.


## Requirements
Docker

Google Cloud https://cloud.google.com/sdk/docs/quickstart#linux

There will be some manual steps to setup Google Cloud so that it allows k8s deploys.


## Setting up

1. Select or create a Google Cloud Platform project

2. [Enable Billing] https://support.google.com/cloud/answer/6293499#enable-billing

3. Use the following commands on your cli:

```
docker pull google/cloud-sdk
docker run -it --name gcloud-config google/cloud-sdk:latest gcloud auth login
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud set project {{project-id}}
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud services enable compute.googleapis.com deploymentmanager.googleapis.com
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud container clusters create pythonapi --region us-west1
```

4. In the GCP console setup and download your access key. Then run ```cat secret.json | base64```. Set this as GKE_SA_KEY in this project.

5. In this project, add GKE_PROJECT as a secret.


### Using Deployment Manager
After your secret key is setup, you can use Deployment Manager to create a more repeatable and customized setup of GKE.
https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/examples/v2/gke 
In the link above is Google's Deployment manager repo for GKE & other resources. Using this repo as a base you can customize your GKE as much as needed. 
