import requests
from requests.auth import HTTPBasicAuth
from config import BASE_URL, USER, PASSWORD, HEADERS

def create_ticket(short_description, description, urgency="3", impact="3"):
    payload = {
        "short_description": short_description,
        "description": description,
        "urgency": urgency,   # 1=High, 2=Medium, 3=Low
        "impact": impact      # 1=High, 2=Medium, 3=Low
    }

    try:
        response = requests.post(BASE_URL,
                                 auth=HTTPBasicAuth(USER, PASSWORD),
                                 headers=HEADERS,
                                 json=payload)
        response.raise_for_status()
        ticket = response.json()["result"]
        print(f"✅ Ticket created: {ticket['number']}")
        print(f"Sys ID: {ticket['sys_id']}")
    except Exception as e:
        print(f"❌ Error creating ticket: {e}")

if __name__ == "__main__":
    create_ticket(
        short_description="Test ticket from Python",
        description="This ticket was created automatically via Python script."
    )
