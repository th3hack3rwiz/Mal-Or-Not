#!/bin/bash
email=$1
filename=$(echo $1 | awk -F "@" '{print $1}')
curl https://ipqualityscore.com/api/json/email/52euadgGvFpxYkflxorqnBTwGY8mEwMi/$1 | jq | grep -E "valid|disposable|smtp_score|dns_valid|deliverability|recent_abuse|fraud_score|leaked|honeypot"  | tr -d "\"," > $filename.report
