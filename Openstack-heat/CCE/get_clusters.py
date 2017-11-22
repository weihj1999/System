#!/usr/bin/python
import CCEUtils

import requests

#url1 = 'https://iam.eu-de.otc.t-systems.com:443/v3/auth/tokens'
token = CCEUtils.get_auth_token()
json = CCEUtils.get_cluster(token)
cluster_id=CCEUtils.get_clusterid(token,"vwcce")
print CCEUtils.get_cluster(token)
print CCEUtils.get_clusterid(token, "vwcce")

#print CCEUtils.update_cluster(token, cluster_id, 'data/cluster_update.json')
