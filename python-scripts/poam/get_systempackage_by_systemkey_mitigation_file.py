#!/usr/bin/env python3
# ============================================================
# OpenRMF Professional External API - Systempackage Mitigation File
# API Path   : GET /systempackage/{systemKey}/mitigation
# Description: Retrieves data from the /systempackage/{systemKey}/mitigation endpoint and saves the response body to a local Excel file.
#
# Required Parameters:
#   1) rootURL            - The base server URL. The script validates it, trims any trailing slash, and appends /api/external automatically.
#   2) applicationKey     - The application key appended to the request URL as the applicationKey query parameter.
#   3) authorizationToken - The bearer token sent as the Authorization request header.
#   4) systemKey          - Required path parameter.
#
# Optional Parameters:
#   outputFile (script option) - Local path to save the downloaded file.
#
# Command Line Example:
#   python3 get_systempackage_by_systemkey_mitigation_file.py \
#       https://example.openrmfpro.local \
#       my-application-key \
#       my-authorization-token \
#       <systemKey>
# ============================================================

import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

import requests
from requests.structures import CaseInsensitiveDict

COMMON_DIR = Path(__file__).resolve().parent.parent / "common"
if str(COMMON_DIR) not in sys.path:
    sys.path.insert(0, str(COMMON_DIR))

from http_status_meanings import HTTP_STATUS_MEANINGS

PATH_TEMPLATE = '/systempackage/{systemKey}/mitigation'
HTTP_METHOD = 'GET'
REQUIRED_POSITIONAL_ARGUMENTS = [
    'systemKey',
]
PATH_PARAMETER_NAMES = [
    'systemKey',
]
REQUIRED_QUERY_PARAMETER_NAMES = []
OPTIONAL_QUERY_PARAMETER_NAMES = []
REQUIRED_BODY_PARAMETER_NAMES = []
OPTIONAL_BODY_PARAMETER_NAMES = []
BINARY_BODY_PARAMETER_NAMES = []
KNOWN_OPTIONAL_NAMES = [
    'outputFile',
]
FILE_EXTENSION_HINT = 'xlsx'
ACCEPT_HEADER = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

# -------------------------------------------------------
# Validate the root URL and normalize it for external API calls
# -------------------------------------------------------
def normalize_root_url(root_url: str) -> str:
    candidate = root_url.rstrip("/")
    parsed = urlsplit(candidate)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        print(f"ERROR: rootURL must be a valid HTTP or HTTPS URL. Provided: {root_url}")
        sys.exit(1)
    if candidate.endswith("/api/external"):
        return candidate
    return f"{candidate}/api/external"

# -------------------------------------------------------
# Replace path parameters and append query parameters to the URL
# -------------------------------------------------------
def build_url(api_root: str, path_values: dict[str, str], query_values: dict[str, str]) -> str:
    rendered_path = PATH_TEMPLATE
    for name in PATH_PARAMETER_NAMES:
        rendered_path = rendered_path.replace("{" + name + "}", quote(str(path_values[name]), safe=""))
    query_string = urlencode(query_values)
    return f"{api_root}{rendered_path}?{query_string}" if query_string else f"{api_root}{rendered_path}"

# -------------------------------------------------------
# Parse KEY=VALUE optional arguments after the required positional args
# -------------------------------------------------------
def parse_optional_arguments(arguments: list[str]) -> dict[str, str]:
    parsed = {}
    for argument in arguments:
        if "=" not in argument:
            print(f"ERROR: Optional arguments must use KEY=VALUE format. Invalid value: {argument}")
            sys.exit(1)
        key, value = argument.split("=", 1)
        parsed[key] = value
    return parsed

# -------------------------------------------------------
# Resolve an output file path for download endpoints
# -------------------------------------------------------
def determine_output_path(options: dict[str, str], system_key: str) -> Path:
    if "outputFile" in options and options["outputFile"].strip():
        return Path(options["outputFile"]).expanduser()

    downloads_root = Path(__file__).resolve().parent.parent / "downloads"
    safe_system_key = str(system_key).replace("/", "_").replace("\\", "_") or "unknown-system"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return downloads_root / f"{safe_system_key}-mitigation-list-{timestamp}.{FILE_EXTENSION_HINT}"

# -------------------------------------------------------
# Validate required arguments and map them to API parameters
# -------------------------------------------------------
minimum_argument_count = 4 + 1
if len(sys.argv) < minimum_argument_count:
    print("ERROR: Missing required parameters.")
    print("Usage: python3 " + Path(__file__).name + " <rootURL> <applicationKey> <authorizationToken>" + (" " + " ".join(f"<{name}>" for name in REQUIRED_POSITIONAL_ARGUMENTS) if REQUIRED_POSITIONAL_ARGUMENTS else "") + (" [KEY=VALUE ...]" if KNOWN_OPTIONAL_NAMES or OPTIONAL_QUERY_PARAMETER_NAMES or OPTIONAL_BODY_PARAMETER_NAMES else ""))
    sys.exit(1)

root_url = sys.argv[1]
application_key = sys.argv[2]
authorization_token = sys.argv[3]
positional_values = sys.argv[4:4 + 1]
optional_values = sys.argv[4 + 1:]

api_root = normalize_root_url(root_url)

path_values = {}
required_query_values = {}
required_body_values = {}

cursor = 0
for name in PATH_PARAMETER_NAMES:
    path_values[name] = positional_values[cursor]
    cursor += 1
for name in REQUIRED_QUERY_PARAMETER_NAMES:
    required_query_values[name] = positional_values[cursor]
    cursor += 1
for name in REQUIRED_BODY_PARAMETER_NAMES:
    required_body_values[name] = positional_values[cursor]
    cursor += 1

optional_arguments = parse_optional_arguments(optional_values)
unknown_optional = sorted(set(optional_arguments) - set(KNOWN_OPTIONAL_NAMES) - set(OPTIONAL_QUERY_PARAMETER_NAMES) - set(OPTIONAL_BODY_PARAMETER_NAMES))
if unknown_optional:
    print("WARNING: Ignoring unrecognized optional parameters: " + ", ".join(unknown_optional))

query_values = {"applicationKey": application_key}
query_values.update(required_query_values)
for name in OPTIONAL_QUERY_PARAMETER_NAMES:
    if name in optional_arguments:
        query_values[name] = optional_arguments[name]

form_data = {}
form_data.update(required_body_values)
for name in OPTIONAL_BODY_PARAMETER_NAMES:
    if name in optional_arguments:
        form_data[name] = optional_arguments[name]

try:
    url = build_url(api_root, path_values, query_values)

    # -------------------------------------------------------
    # Build the Authorization header and any endpoint-specific headers
    # -------------------------------------------------------
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {authorization_token}"
    if ACCEPT_HEADER:
        headers["Accept"] = ACCEPT_HEADER

    request_kwargs = {"headers": headers, "stream": True}
    if form_data:
        request_kwargs["data"] = form_data

    # -------------------------------------------------------
    # Execute the HTTP request
    # -------------------------------------------------------
    print(f"Calling {HTTP_METHOD} {url} ...")
    response = requests.request(HTTP_METHOD, url, **request_kwargs)
except requests.exceptions.RequestException as exc:
    print(f"ERROR: The request failed before a response was received. Details: {exc}")
    sys.exit(1)

# -------------------------------------------------------
# Save a successful response body to a local file
# -------------------------------------------------------
if 200 <= response.status_code < 300:
    output_path = determine_output_path(optional_arguments, path_values["systemKey"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as handle:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                handle.write(chunk)
    print(f"Downloaded file saved to {output_path}")
else:
    meaning = HTTP_STATUS_MEANINGS.get(response.status_code, "Unexpected status code returned by the server.")
    print(f"ERROR: HTTP {response.status_code} - {meaning}")
    print(response.text)
    sys.exit(1)