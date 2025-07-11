# Download a system package checklist CKL file
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/checklist/{checklistId}/?applicationKey={applicationKey}
# ex: python3 downloadChecklist.py http://192.168.13.111:8080 companyinfra 627d44fbff17ea6dfdf0d702 openrmfprosvc hvs.xxxxxxxxxxx > ../download/mychecklist.ckl

import sys
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/checklist/" + sys.argv[3] + "/?format=ckl&applicationKey=" + sys.argv[4]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/xml;charset=utf-8"
headers["Authorization"] = "Bearer " + sys.argv[5]
resp = requests.get(url, headers=headers)

print(resp.text)