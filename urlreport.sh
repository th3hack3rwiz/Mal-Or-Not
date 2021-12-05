#!/bin/bash
name=$(echo $1 | awk -F "/" '{print $3}')
curl --request POST --url https://www.virustotal.com/api/v3/urls --header 'x-apikey: d2d01393e9c34f7d20d08625f1aa6409e8323a9765568dc88a38a2a330213f2>
id=$(cat result1 | jq | grep id | awk -F "\"" '{print $4}')
rm result1
curl --request GET --url https://www.virustotal.com/api/v3/analyses/$id --header 'x-apikey: d2d01393e9c34f7d20d08625f1aa6409e8323a9765568dc88a38a2a3>
echo -e "\nAccording to VirusTotal API:\n"  | tee $name.report
cat result2 | jq | grep -E "harmless|malicious|suspicious|undetected" | grep -iEv "Result|category" | tr -d "\"" | sed 's/\<\([[:lower:]]\)\([[:alnu>
#phishing_count=$(cat result2 | grep phishing | grep result | wc -l)
#malware_count=$(cat result2 | grep malware | grep result | wc -l)
#echo -e "\tMalware: $malware_count"
#echo -e "\tPhishing: $phishing_count"
malicious_sources=$(cat result2 | grep malicious -B 2 | grep -v malicious | grep -E "[[:alpha:]]" | grep -vE "stats|harmless" | tr -d "\":{")
if [ -z "$malicious_sources" ];
then echo lol >/dev/null
else
echo -e "\nResult:" | tee -a $name.report
for i in $(echo $malicious_sources); do echo -e "\t$i - $(cat result2| grep $i -A 2  | grep result | tr -d '\",' | awk '{print $2}')" | tee -a $name>
fi
rm result2
