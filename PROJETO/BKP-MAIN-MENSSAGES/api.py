from oauth2client import client, file, tools
from httplib2 import Http
from apiclient import discovery
import json

API_KEY = 'AIzaSyCgKweSooEq5Fa_DyUofztnGpidWJFbCHI'
FORM_ID = '1M-PFqUofBpEbmC4_NsX80B34nHK0jDBLVZWr9tzpVD0'

SCOPES = ['https://www.googleapis.com/auth/drive']
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("client_secrets.json")
creds = None

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("client_secrets.json", SCOPES)
    creds = tools.run_flow(flow, store)
    print(creds)

service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

# Prints the title of the sample form:
form_id = FORM_ID
result = service.forms().get(formId=form_id).execute()

# Imprime os resultados formatados
print(json.dumps(result, indent=2))
