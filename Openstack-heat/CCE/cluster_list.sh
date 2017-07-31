#!/bin/bash -v
#post for token
token=$(curl -0 -iv -X POST -v -H "content-type=application/json" https://iam.eu-de.otc.t-systems.com:443/v3/auth/tokens -d @data/auth.json 2>&1 | grep -m 1 -oP '(?<=X-Subject-Token:\s).*')

echo $token
#create cluster
#curl -X GET -v -H "Content-Type: application/json" -H "X-Auth-Token: $token" https://cce.eu-de.otc.t-systems.com/api/v1/clusters | sed -e 's/[{}]/''/g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' 
export PYTHONIOENCODING=utf8
curl -X GET -v -s -H "Content-Type: application/json" -H "X-Auth-Token: $token" https://cce.eu-de.otc.t-systems.com/api/v1/clusters | python -c "import sys, json; print json.loads(sys.stdin)" 

#set th


