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

There will be some partially manual steps to setup Google Cloud so that it allows k8s deploys.

(It could be possible that this is all fully automatable).

### Setting up the project to deploy from GitHub to GKE
Assuming you have a project & your service account setup is complete.
you will need to bake in your json api key as a secret. You can pull the key, and the cat secret.json | base64 and input it as a secret.
You will also need to setup your GKE project as a secret so the pipeline can pull it.

### Setting up GCloud for the deploy using the cli
For now, to get GCloud setup enough to run the scripts, using the GCloud cli, do the following:

docker pull google/cloud-sdk

docker run google/cloud-sdk:latest gcloud version

docker run -it --name gcloud-config google/cloud-sdk:latest gcloud auth login

Create a GCloud rule to allow ingress on port 5000
gcloud compute firewall-rules create my-rule --allow=tcp:5000

Login to your Gcloud account and input your code to it.

docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud projects create liatrio1

docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud config set project liatrio1

Login to your Gcloud account and enable billing through the Kubernets panel

docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud container clusters create pythonapi --region us-west1

### Using Deployment Manager
After your project has been created, and your secret key is setup, you can use Deployment Manager to create a more repeatable and customized setup of GKE.
https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/examples/v2/gke 
In the link above is Google's Deployment manager repo for GKE. Using this repo as a base you can customize your GKE as much as needed.
