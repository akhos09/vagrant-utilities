#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip pipx
python3 --version
pipx ensurepath
pip3 install ansible --user
mkdir -p /root/.ssh && cd /root/.ssh
echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
echo -e "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
sudo ssh-keygen -t rsa -b 2048 -f id_rsa
python3 -m http.server 80 &
useradd -m ansible
passwd -e ansible
sudo -u ansible ssh-keygen
echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
#all changes here