import requests
import json
from mock import Mock
BASE_URL = "https://dev06.xcl.ie"
response = requests.get(BASE_URL)
#print(response)
print(json.dumps(response.json(), indent=4))
