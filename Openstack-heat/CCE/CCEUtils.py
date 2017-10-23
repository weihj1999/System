import urllib2
import json
import requests

#######################################################################
#For all the service endpoints which are support in OTC, Please refer to 
#https://docs.otc.t-systems.com/en-us/endpoint/index.html
#######################################################################

IAM_DE_ENDPOINT = "https://iam.eu-de.otc.t-systems.com"
IAM_SG_ENDPOINT = "https://iam.ap-sg.otc.t-systems.com"
CCE_DE_ENDPOINT = "https://cce.eu-de.otc.t-systems.com"

def get_auth_token():
    '''
    get an auth token
    '''
    url = IAM_DE_ENDPOINT + '/v3/auth/tokens'
    headers = {'Content-Type': 'application/json'}
    data = open('data/auth-1.json','rb')

    r = requests.post(url, data, headers)
    return r.headers.get('X-Subject-Token')

def get_cluster(auth_token):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    return pjson

def get_clusterstatus(auth_token, clustername):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    for d in pjson:
      if d['metadata']['name'] == clustername:
         return d['metadata']['clusterStatus']

def get_clusterid(auth_token, clustername):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    for d in pjson:
      if d['metadata']['name'] == clustername:
         return d['metadata']['uuid']

def get_cacrt(auth_token, cluster_id):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/' + cluster_id + '/certificates'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    return pjson['cacrt']

def get_clientcrt(auth_token, cluster_id):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/' + cluster_id + '/certificates'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    return pjson['clientcrt']

def get_clientkey(auth_token, cluster_id):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/' + cluster_id + '/certificates'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    r = requests.get(url, headers=headers)
    pjson = json.loads(r.text)
    return pjson['clientkey']

def create_cluster(auth_token, content):
    '''
      returns json object with info
    '''
    data = open(content,'rb')
    url = CCE_DE_ENDPOINT + '/api/v1/clusters'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    resp = requests.post(url, data, headers=headers)
    if resp.status_code == requests.codes.created:
        result = True
    else:
        result = False
    return result

def update_cluster(auth_token, cluster_id, content):
    '''
      returns json object with info
    '''
    data = open(content,'rb')
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/' + cluster_id
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    #import pdb; pdb.set_trace()
    resp = requests.put(url, data, headers=headers)
    if resp.status_code == requests.codes.ok:
        result = True
    else:
        result = False
    return result

def delete_cluster(auth_token, cluster_id):
    '''
      returns json object with info
    '''
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/' + cluster_id
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    import pdb; pdb.set_trace()
    resp = requests.delete(url, headers=headers)
    return resp.text


def add_nodes(auth_token, cluster_id, content):
    '''
      returns json object with info
    '''
    data = open(content,'rb')
    url = CCE_DE_ENDPOINT + '/api/v1/clusters/'+cluster_id + '/hosts'
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    import pdb; pdb.set_trace()
    resp = requests.post(url, data=data, headers=headers)
    if resp.status_code == requests.codes.created:
	result = True
    else:
        result = False
    return result
