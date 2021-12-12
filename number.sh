number=$1
curl -s "http://apilayer.net/api/validate?access_key=NNNN&number=$number&format=1" | grep -E "valid|local_format|international_format|country_prefix|country_code|country_name|location|carrier|line_type" | tr -d "\"," | sed 's/:/ : /g' > $number.number.report
echo -e "Number: $1\n" >> number.report
cat $number.report >> number.report
echo -e "\n" >> number.report
