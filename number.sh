number=$1
curl "http://apilayer.net/api/validate?access_key=NNNN&number=$number&format=1" | grep -E "valid|local_format|international_format|country_prefix|country_code|country_name|location|carrier|line_type" | tr -d "\"," | sed 's/:/ : /g' | tee  $number.report
