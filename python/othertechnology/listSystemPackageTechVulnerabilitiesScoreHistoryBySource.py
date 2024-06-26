# score history of a particular source project for the other technology vulnerabilities
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/techvulnerabilityscorehistory/{categoryType}/source/{sourcename}/project/{projectname}/?applicationKey={applicationKey}
# ex: python3 listSystemPackageTechVulnerabilitiesScoreHistoryBySource.py http://192.168.13.111:8080 companyinfra 10 sourcename projectname openrmfprosvc hvs.xxxxxxxxxxxxxx

import sys
import json
import requests
from requests.structures import CaseInsensitiveDict

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2]+ "/techvulnerabilityscorehistory/" + sys.argv[3] + "/source/" + sys.argv[4] + "/project/" + sys.argv[5] + "/?applicationKey=" + sys.argv[6]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + sys.argv[7]

resp = requests.get(url, headers=headers)

# print(resp.status_code)
# print(resp.text)

json_object = json.loads(resp.text)
print(json.dumps(json_object, indent=1))