#!/bin/bash
sudo service docker start
sudo docker build -t src .
sudo docker run -p 8000:8000 src