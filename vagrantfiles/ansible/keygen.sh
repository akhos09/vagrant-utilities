#!/bin/bash setup ssh
sudo apt-get update && sudo apt-get upgrade -y
cd /root/.ssh
ssh-copy-id -i keysshnodemaster root@192.168.30.3