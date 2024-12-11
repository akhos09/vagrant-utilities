#!/bin/bash
#ANSIBLE INSTALL
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip pipx
python3 --version
pipx ensurepath
pip3 install ansible --user
#SSH ROOT
mkdir -p /root/.ssh && cd /root/.ssh
echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
echo -e "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
sudo ssh-keygen -t rsa -b 2048 -f id_rsa
#SSH ANSIBLE USER
useradd -m ansible -s /bin/bash
passwd -d ansible
sudo -u ansible mkdir -p /home/ansible/.ssh
cd /home/ansible/.ssh
sudo -u ansible ssh-keygen -f id_rsa2
sudo mv ./id_rsa2.pub /root/.ssh/id_rsa2.pub
cd /root/.ssh/
echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
python3 -m http.server 80 &
#all changes here