FROM google/cloud-sdk

COPY .auth/liatrio1-0db366aa2410.json .
RUN gcloud auth activate-service-account 19621962216-compute@developer.gserviceaccount.com --key-file liatrio1-0db366aa2410.json --project=testproject
RUN gcloud config set project liatrio1
RUN gcloud container clusters create pythonapi --region us-west1