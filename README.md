# python-api
This is a simple python api meant to be deployed in docker, and then k8s.

## Architecture

## Requirements
Docker
Google Cloud https://cloud.google.com/sdk/docs/quickstart#linux
There will be some partially manual steps to setup Google Cloud so that it allows k8s deploys.
(It could be possible that this is all fully automatable).

Assuming you have a project & your service account setup is complete.
you will need to bake in your json api key.

For now, to get GCloud setup enough to run the scripts, do the following:
docker pull google/cloud-sdk
docker run google/cloud-sdk:latest gcloud version
docker run -it --name gcloud-config google/cloud-sdk:latest gcloud auth login
Login to your Gcloud account and input your code to it.
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud projects create liatrio1
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud config set project liatrio1
Login to your Gcloud account and enable billing through the Kubernets panel
docker run --volumes-from gcloud-config -it google/cloud-sdk:latest gcloud container clusters create pythonapi --region us-west1

Run deploy-gcloud.sh