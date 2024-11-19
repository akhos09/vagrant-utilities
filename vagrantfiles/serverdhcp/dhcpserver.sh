#!/bin/bash
#:Title: dhcpforge.sh
#:Version: 1.0
#:Author: Pablo Fernández López
#:Date: 19/04/2024
#:Dependencies:
#:      - "ISC-DHCP-SERVER"
routerfunc(){
    sudo echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
    sudo sysctl -p
    sudo iptables -t nat -A POSTROUTING -s 10.33.200.0/24 -o enp0s8 -j SNAT --to-source 172.19.200.67
}
install_dhcp_server(){
   ens="enp0s9"
   sudo apt-get update && sudo apt-get upgrade -y
   sudo apt-get install isc-dhcp-server
   echo -e "Copying the file isc-dhcp-server in /etc/default/isc-dhcp-server.copy..."
   sudo cp /etc/default/isc-dhcp-server /etc/default/isc-dhcp-server.copy
   
   config_file="/etc/default/isc-dhcp-server"
   if [ -f "$config_file" ]; then
       sudo sed -i "s/^INTERFACESv4=.*/INTERFACESv4=\"$ens\"/" "$config_file"
   else
       echo "Error: $config_file doesn't exist."
   fi
   service isc-dhcp-server restart
   sudo ifconfig $ens down
   sudo ifconfig $ens up
}

configure_dhcp_server(){
    ens="enp0s9" 
    #MODIFY THIS AS YOU WANT
    subnet="10.33.200.0"
    netmask="255.255.255.0"
    router="10.33.200.1"
    dns="8.8.8.8,1.1.1.1"
    range_start="10.33.200.50"
    range_end="10.33.200.100"
   
   #CHECK CONFIG FILES
   config_file="/etc/dhcp/dhcpd.conf"
   if [ ! -f "$config_file" ]; then
       echo "Error: The $config_file doesn't exist."
       exit 1
   fi
   config_file="/etc/default/isc-dhcp-server"
   if [ -f "$config_file" ]; then
       sudo sed -i "s/^INTERFACESv4=.*/INTERFACESv4=\"$ens\"/" "$config_file"
   else
       echo "Error: $config_file doesn't exist."
   fi

   config_dhcp="subnet $subnet netmask $netmask {
     option routers $router;
     option subnet-mask $netmask;
     option domain-name-servers $dns;
     range $range_start $range_end;
   }"

   echo "option domain-name \"example.org\";" | sudo tee "$config_file" > /dev/null
   echo "option domain-name-servers ns1.example.org, ns2.example.org;" | sudo tee -a "$config_file" > /dev/null
   echo "default-lease-time 600;" | sudo tee -a "$config_file" > /dev/null
   echo "max-lease-time 7200;" | sudo tee -a "$config_file" > /dev/null
   echo "ddns-update-style none;" | sudo tee -a "$config_file" > /dev/null
   echo -e "\n$config_dhcp" | sudo tee -a "$config_file" > /dev/null

      echo "DHCP configuration updated in $config_file."

      sudo systemctl restart isc-dhcp-server
      sudo dhcp-lease-list --lease /var/lib/dhcp/dhcpd.leases | awk '{print $3}' | while read ip; do
      ping -c 1 $ip &> /dev/null && ssh -o ConnectTimeout=2 $ip "sudo dhclient -r && sudo dhclient" &
   done
}

routerfunc

install_dhcp_server

configure_dhcp_server
