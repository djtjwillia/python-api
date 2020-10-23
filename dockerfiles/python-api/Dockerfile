FROM python:3.8

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app/ app/

EXPOSE 5000

# command to run on container start
CMD [ "flask", "run", "--host", "0.0.0.0" ]
