#!/bin/bash
sudo apt install python3-pip
sudo apt-get install jq
sudo apt-get install speedtest-cli
pip install python-whois
pip install fpdf
pip install futures
pip install PySocks
sudo apt-get install figlet
chmod +x number.sh
chmod +x email.sh
read -p "Enter ip2location API key:" ip2location
read -p "Enter ipqualityscore API key:" ipquality
read -p "Enter virustotal API key:" virustotal
read -p "Enter numverify API key:" numverify
sed -i "s#XXXX#$virustotal#" urlreport.sh
sed -i "s#XXXX#$virustotal#" file.sh
sed -i "s#YYYY#$ip2location#" ipintel.sh
sed -i "s#ZZZZ#$ipquality#" ipintel.sh
sed -i "s#ZZZZ#$ipquality#" WhoIsInfo.py
sed -i "s#NNNN#$numverify#" number.sh
chmod +x ipintel.sh
chmod +x urlreport.sh
chmod +x speedtest.sh
chmod +x file.sh
mkdir -p output/ip
mkdir output/domain
mkdir output/number
mkdir output/url
mkdir output/file
mkdir output/email
mkdir -p reports/ip
mkdir reports/domain
mkdir reports/number
mkdir reports/url
mkdir reports/file
mkdir reports/email
