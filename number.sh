number=$1
echo  "Number: $1\n\nResult:" > output/number/$number.number.report
printf "\n" >> output/number/$number.number.report
curl -s "http://apilayer.net/api/validate?access_key=NNNN&number=$number&format=1" | grep -E "valid|local_format|international_format|country_prefix|country_code|country_name|location|carrier|line_type" | tr -d "\"," | sed 's/:/ : /g' >> output/number/$number.number.report
cat output/number/$number.number.report >> output/number/number.master.report
echo -e "\n" >> output/number/number.master.report
                                                     
