#!/bin/bash
#Initial commands that are a must-execute.
apt-get update && apt-get upgrade -y
sudo iptables -t nat -A POSTROUTING -s 10.33.200.0/24 -o enp0s8 -j SNAT --to-source 172.19.200.67