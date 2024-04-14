#!/bin/bash

# Install Chromedriver
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
   mkdir -p ~/chromedriver-$CHROMEDRIVER_VERSION && \
   curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
   unzip -qq /tmp/chromedriver_linux64.zip -d ~/chromedriver-$CHROMEDRIVER_VERSION && \
   rm /tmp/chromedriver_linux64.zip && \
   chmod +x ~/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
   ln -fs ~/chromedriver-$CHROMEDRIVER_VERSION/chromedriver ~/bin/chromedriver

# Install Google Chrome
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
   echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee ~/.local/google-chrome.list && \
   apt-get -yqq update && \
   apt-get -yqq install google-chrome-stable && \
   rm -rf /var/lib/apt/lists/*

# Install dependencies
apt-get update && apt-get install -y \
  unzip \
  curl \
  gnupg
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo deb "http://dl.google.com/linux/chrome/deb/ stable main" >> ~/.local/google-chrome.list
apt-get -y update
apt-get install -y google-chrome-stable
