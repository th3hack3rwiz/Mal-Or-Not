#!/bin/bash
email=$1
filename=$(echo $1 | awk -F "@" '{print $1}')
echo -e "E-mail Address: $email\n\nResult:">output/email/$filename.email.report
curl -s https://ipqualityscore.com/api/json/email/52euadgGvFpxYkflxorqnBTwGY8mEwMi/$1 | jq | grep -E "valid|disposable|smtp_score|dns_valid|deliverability|recent_abuse|fraud_score|leaked|honeypot"  | tr -d "\"," >> output/email/$filename.email.report
cat output/email/$filename.email.report >> output/email/email.master.report
echo -e "\n" >> output/email/email.master.report
