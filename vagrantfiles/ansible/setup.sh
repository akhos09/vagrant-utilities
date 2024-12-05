#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip pipx
python3 --version
pipx ensurepath
pip3 install ansible --user
sudo ssh-keygen -t rsa -b 2048 -f keysshnodemaster
sudo reboot
#all changes here