#!/bin/bash -v
#post for token
token=$(curl -0 -iv -X POST -v -H "content-type=application/json" https://iam.eu-de.otc.t-systems.com:443/v3/auth/tokens -d @myauth.json 2>&1 | grep -m 1 -oP '(?<=X-Subject-Token:\s).*')

echo $token
curl -XPUT -v -H "X-Auth-Token: $token" https://vpc.eu-de.otc.t-systems.com/v2.0/routers/d4033e4b-84b1-464a-a99c-b3f889d48b07 -d @myrouter.json


#set th


