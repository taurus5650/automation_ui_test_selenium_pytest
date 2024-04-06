#FROM --platform=linux/amd64 python:3.11-slim-buster
#
#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/
#
#COPY . /usr/src/app/
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#
#RUN apt --fix-broken install \
#  && apt-get update \
#  && apt-get install -y wget \
#  && apt-get install -y gnupg2 \
#  && apt-get install -y curl \
#  && apt-get install -yqq unzip \
#  && rm -rf /var/lib/apt/lists/*
#
## install google chrome
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
#RUN apt-get -y update
#RUN apt-get install -y google-chrome-stable
#
## install chromedriver
#
#RUN wget -O /tmp/chromedriver.zip https://old.chromedriver.com/113.0.5672.63/chromedriver_linux64.zip \
#    && unzip -o /tmp/chromedriver.zip -d /usr/src/app/chromedriver/ \
#    && rm /tmp/chromedriver.zip
#
#
##RUN apt-get install -yqq unzip
##RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
##    && unzip -o /tmp/chromedriver.zip -d /usr/src/app/chromedriver/
#
#CMD tail -f /dev/null
#
#
#CMD pytest -v -s


# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set an environment variable to indicate that we are running inside Docker
ENV RUNNING_IN_DOCKER=true

CMD tail -f /dev/null