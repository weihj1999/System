#!/bin/bash -v
#post for token
token=$(curl -0 -iv -X POST -v -H "content-type=application/json" https://iam.eu-de.otc.t-systems.com:443/v3/auth/tokens -d @data/auth.json 2>&1 | grep -m 1 -oP '(?<=X-Subject-Token:\s).*')

echo $token
#create cluster
curl -X POST -v -H "Content-Type: application/json" -H "X-Auth-Token: $token" https://cce.eu-de.otc.t-systems.com/api/v1/clusters -d @data/cluster.json

#set th


