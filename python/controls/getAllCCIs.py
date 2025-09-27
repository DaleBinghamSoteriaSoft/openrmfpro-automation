# get all the CCIs
# API call from Developer's Guide: /api/external/ccis/?applicationKey={applicationKey}
# ex: python3 getAllCCIs.py http://192.168.13.111:8080 openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

if len(sys.argv) < 4:
    print("Usage: python3 getAllCCIs.py <URL> <applicationKey> <token>")
    sys.exit(1)

base_url = sys.argv[1]
app_key = sys.argv[2]
token = sys.argv[3]

endpoint = "/api/external/ccis/"
url = f"{base_url}{endpoint}"

params = {
    "applicationKey": app_key
}

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {token}"

try:
    resp = requests.get(url, headers=headers, params=params)
    
    print(f"HTTP Status Code: {resp.status_code}")

    if resp.status_code == 200:
        json_object = resp.json()
        print(json.dumps(json_object, indent=1))
    else:
        print("Error retrieving all CCIs:")
        print(resp.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API call: {e}")