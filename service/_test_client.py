#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        'method': "hold",
        'params': ["Belgium"],
        'jsonrpc': "2.0",
        'id': 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, auth=HTTPBasicAuth('loli', 'loli'))

    print response
    
    response = response.json()
    
    print response

    print response['result']
    print response['jsonrpc']
    print response['id'] == 0

if __name__ == "__main__":
    main()