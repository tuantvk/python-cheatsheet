# Call JIRA API with HTTPBasicAuth
import json
import requests
from requests.auth import HTTPBasicAuth

# config here
# view more: https://developer.atlassian.com

JIRA_EMAIL = "email@domain.com"
JIRA_TOKEN = "jira_token...."
BASE_URL = "https://domain.atlassian.net"
API_URL = "/rest/api/3/issue/TYPE-425"

API_URL = BASE_URL+API_URL

BASIC_AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)
HEADERS = {'Content-Type' : 'application/json;charset=iso-8859-1'}

response = requests.get(
  API_URL,
  headers=HEADERS,
  auth=BASIC_AUTH
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))