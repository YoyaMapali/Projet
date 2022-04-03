#!/bin/bah
##installation de mariadb
sudo yum install -y mariadb
sudo yum install -y mariadb-server
echo ' start '
## creation et demarrage du service
sudo systemctl enable mariadb.service
sudo systemctl start mariadb