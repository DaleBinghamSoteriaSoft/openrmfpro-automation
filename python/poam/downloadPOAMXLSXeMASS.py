# Get the actual MS Excel file of the Plan of Action and Milestones listing and save to a file
# API call from Developer's Guide: /api/external/systempackage/{systemKey}/poam/?applicationKey={applicationKey}&days=365&devicename=sot-win2k22
# ex: python3 downloadPOAMXLSXeMASS.py http://192.168.13.111:8080 companyinfra openrmfprosvc hvs.xxxxxxxxx

import sys
import requests
from requests.structures import CaseInsensitiveDict
import os

url = sys.argv[1] + "/api/external/systempackage/" + sys.argv[2] + "/poam/?applicationKey=" + sys.argv[3]

headers = CaseInsensitiveDict()
headers["Accept"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
headers["Authorization"] = "Bearer " + sys.argv[4]

resp = requests.get(url, headers=headers)
filename = sys.argv[2] + "-POAM-eMASS.xlsx"
filepath = '../download/'
file_path = os.path.join(filepath, filename)
r = requests.get(url, headers=headers, stream=True)
if r.ok:
  print("saving to", os.path.abspath(file_path))
  with open(file_path, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024 * 8):
      if chunk:
        f.write(chunk)
        f.flush()
        os.fsync(f.fileno())
else:  # HTTP status code 4XX/5XX
  print("Download failed: status code {}\n{}".format(r.status_code, r.text))

print(resp.status_code)
print("Request Completed")