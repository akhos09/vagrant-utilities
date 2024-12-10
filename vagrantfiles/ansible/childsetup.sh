#!/bin/bash
#setup ssh
sudo apt-get update && sudo apt-get upgrade -y
echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
echo -e "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
mkdir -p /root/.ssh && cd /root/.ssh
wget http://192.168.30.3/id_rsa.pub
cat id_rsa.pub >> authorized_keys
useradd -m ansible
passwd -e ansible
sudo -u ansible wget http://192.168.30.3/../../ansible/.ssh/id_rsa.pub
cd /home/ansible/.ssh
cat id_rsa.pub >> authorized_keys