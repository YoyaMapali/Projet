#!/bin/bash
####installation de iredMail depuis github
sudo wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz
###decompressio du fichier avec tar
tar -xwvf 1.5.2.tar.gz
###se deplacer et rendre le script executable
cd /1.5.2.tar.gz
chmod a+x iRedMail
executer le script
./iResMail.sh