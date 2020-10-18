#!/bin/bash
helpFunction()
{
   echo ""
   echo "Usage: $0 -t tag -v version"
   echo -e "\t-t Tag for the docker image"
   echo -e "\t-v Version for the docker image"
   exit 1 # Exit script after printing help
}

while getopts "t:v:" opt
do
   case "$opt" in
      t ) docker_tag="$OPTARG" ;;
      v ) docker_version="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

if [ -z "$docker_tag" ] || [ -z "$docker_version" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

docker run -p 5000:5000 $docker_tag:$docker_version