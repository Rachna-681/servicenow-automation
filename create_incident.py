import json
import requests

BASE_URL = f"https://dev192259.service-now.com/api/now/table/incident"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


payload = {
    "short_description": "This is coimng from python",
    "description": "This is my first ticket created",
    "urgency": 1,   # 1=High, 2=Medium, 3=Low
    "impact": "High"      # 1=High, 2=Medium, 3=Low
    }
response = requests.post(BASE_URL,
                         auth=("admin", "ytpI4iEY^A-7"),
                         headers=HEADERS,
                         json=payload)
print(response.text)

