#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip
python3 --version
pip3 install ansible --user
sudo ssh-keygen -t rsa -b 2048 -f keysshnodemaster