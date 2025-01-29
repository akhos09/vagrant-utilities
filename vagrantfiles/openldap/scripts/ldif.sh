#!/bin/bash

read -p "Enter the name of the .ldif file you want to apply: " file
read -p "Domain name (without ies or es, etc.): " dn1
read -p "Domain name (ies, es, etc.): " dn2

output=$(ldapsearch -VV 2>&1)
if [ $? -eq 0 ]; then
    echo -e "-------------------------------------------------------"
    ldapadd -x -H ldap://localhost -D "cn=admin,dc=$dn1,dc=$dn2" -W  -f "$file"
    if [ $? -eq 0 ]; then
        echo -e ".ldif file applied successfully"
    else
        echo -e "An error has occurred during the execution of the command. Check syntax or logs."
    fi
else
    echo -e "LDAP not installed or doesn't work properly."
    echo -e "\n"
    echo -e "$output"
fi

