#!/bin/bash
cd /root/ansible/
ansible -i machines node2 node3 -m shell -a "df -h" > filesystem_nodes2_3.log
ansible -i machines all -m shell -a "free -h" > memoryallnodes.log
ansible -i machines node1 -m shell -a "awk -F: '$NF == "/bin/bash" {print $1}' /etc/passwd > usersbashnode1.log"
