#!/bin/bash
helpFunction()
{
   echo ""
   echo "Usage: $0 -t tag -v version"
   echo -e "\t-t Tag for the docker image"
   echo -e "\t-v Version for the docker image"
   echo -e "\t-a App we are building"
   exit 1 # Exit script after printing help
}

while getopts "t:v:a:" opt
do
   case "$opt" in
      t ) docker_tag="$OPTARG" ;;
      v ) docker_version="$OPTARG" ;;
      a ) docker_app="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

if [ -z "$docker_tag" ] || [ -z "$docker_version" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

docker run --rm -i hadolint/hadolint < dockerfiles/$docker_app/Dockerfile

docker build -t $docker_tag:$docker_version -f dockerfiles/$docker_app/Dockerfile .