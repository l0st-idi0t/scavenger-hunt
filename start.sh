#!/bin/bash
sudo service docker start
sudo docker build -t src .
sudo docker run -p 8080:80 src
