# Example Code for Python 3.x to push and pull data from OpenRMF<sup>&reg;</sup> Professional
The examples here assume you have OpenRMF<sup>&reg;</sup> Professional installed, the external API setup and turned on, and you have at least one Application Integration record setup on the Administration --> External API Integration page. Your user account in Keycloak also must be setup to match the API integration with proper roles and permissions, including the ExternalAPI role to allow interaction from outside the OpenRMF<sup>&reg;</sup> Professional UI.

Some of the APIs for patch vulnerabilities and the other technology vulnerabilities are version 2.8 or higher. Evidence Management was added in v2.9.  If you have questions please see your customer representative or email Soteria Software Support. You can also contact us on our https://www.soteriasoft.com/ company website as well.

## Install Requests Python Package

You will need to run `pip3 install requests` in order to load that library into your folder. Then you can start with the authentication.py script.

## Install prettytable Python Package

You will need to run `pip3 install prettytable` in order to load that library into your folder. Then you can start with the authentication.py script.

## Install the Python Keycloak library

You will need to run `pip install python-keycloak` to add the proper library into your folder to call Keycloak with the scripts. See https://pypi.org/project/python-keycloak/ for more great information.  Those specific examples are under <a href="./keycloak/python-keycloak-lib/">python/keycloak/python-keycloak-lib/</a> specifically. 

## MacOS Installation

You may need to run this to setup requests and call the Python3 scripts correctly in a virtual environment.

```
python3 -m venv {{ path/to/venv }}
source {{ path/to/venv/}}bin/activate
python3 -m pip install requests
```

An example is below

```
➜  scripts git:(main) ✗ python3 -m venv ./.env/

➜  scripts git:(main) ✗ source ./.env/bin/activate

(.env) ➜  scripts git:(main) ✗ python3 -m pip install requests prettytable
Collecting requests
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.6-cp313-cp313-macosx_10_13_universal2.whl.metadata (40 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading charset_normalizer-3.4.6-cp313-cp313-macosx_10_13_universal2.whl (294 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
Successfully installed certifi-2026.2.25 charset_normalizer-3.4.6 idna-3.11 requests-2.32.5 urllib3-2.6.3

[notice] A new release of pip is available: 25.0 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
(.env) ➜  scripts git:(main) ✗ 
```

## Testing Authentication

To ensure your authentication is valid using the simple script for testauthentication.sh in the <a href="../scripts/">scripts</a> folder and make sure it prints back 200 as the request status. If so then your API call, structure, API Key, Token and user/pwd combination for that API are all valid.

## API Calls

The API calls here follow the OpenRMF<sup>&reg;</sup> Professional Developer's Guide. Please contact <a href="https://www.soteriasoft.com/resources/contact.html">Soteria Software</a> for more information.

## Example bulk add Python script
This would load up workstations named SOTWKS2000001 to 00581 with 6 checklists per workstation. These are based on the image we push out for Windows desktops, so a good starting point to see where we are when deployed. Then scans are updated and uploaded to track from there forward.

```
python3 windowsdesktopstackbulk.py http://192.168.13.100:8080/ company-desktop-infra myapiaccountname hvs.87587659786LKGJKHGLJKHJK "652fcdccde4e9aef5c32545b,652fcdeede4e9aef5c32545e,652fcdfdde4e9aef5c32545f,652fcdc1de4e9aef5c32545a,652fcdd7de4e9aef5c32545c,652fcde1de4e9aef5c32545d" SOTWKS200 1 581
```

## MacOS Sonoma

You may need to run this to setup requests and call the Python3 scripts correctly.

```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install requests
```

## Notes
* for the Download XLSX scripts, there needs to be a ./download/ directory created where you run it. Or modify as appropriate.
* we tried to put the applicable scripts into the appropriate folders for organization
* titles (hopefully) are self explanatory
* there is an example call in each `.py` file
