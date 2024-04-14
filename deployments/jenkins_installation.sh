#!/bin/bash

# Install Chromedriver
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
   mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
   curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
   unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
   rm /tmp/chromedriver_linux64.zip && \
   chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
   ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - && \
   echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list && \
   sudo apt-get -yqq update && \
   sudo apt-get -yqq install google-chrome-stable && \
   sudo rm -rf /var/lib/apt/lists/*

# Install dependencies
sudo apt-get update && sudo apt-get install -y \
  unzip \
  curl \
  gnupg
sudo curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
sudo echo deb "http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get install -y google-chrome-stable
