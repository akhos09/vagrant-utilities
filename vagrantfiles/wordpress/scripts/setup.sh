#!/bin/bash
set -x 

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install apache2 php mysql-server php-mbstring php-zip php-gd php-json php-curl openssl -y

sudo tee /etc/php/8.1/apache2/php.ini > /dev/null << 'EOF'
display_errors = On
display_startup_errors = On
error_reporting = E_ALL
log_errors = On
error_log = /var/log/php_errors.log
memory_limit = 256M
max_execution_time = 300
upload_max_filesize = 64M
post_max_size = 64M
extension=curl
extension=mbstring
extension=mysqli
extension=openssl
extension=pdo_mysql
extension=gd
date.timezone = Europe/Madrid
opcache.enable = 0
default_charset="ES"
EOF

sudo systemctl restart apache2
echo "<?php phpinfo ();?>" > /var/www/html/version.php

cd /etc/ssl/certs
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt -subj "/CN=wppablo.local" -addext "subjectAltName=DNS:wppablo.local"
sudo a2enmod ssl

sudo tee /etc/apache2/sites-available/cert.conf > /dev/null << 'EOF'
<VirtualHost *:443>

        ServerName wppablo.local

        DocumentRoot /var/www/html


        SSLEngine on

        SSLCertificateFile /etc/ssl/certs/server.crt

        SSLCertificateKeyFile /etc/ssl/certs/server.key


        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF
sudo a2ensite cert.conf
sudo systemctl restart apache2
sudo cp /etc/ssl/certs/server.crt /usr/local/share/ca-certificates/server.crt
sudo update-ca-certificates
sudo reboot