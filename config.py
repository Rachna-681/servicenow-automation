import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

INSTANCE = os.getenv("SERVICENOW_INSTANCE")
USER = os.getenv("SERVICENOW_USER")
PASSWORD = os.getenv("SERVICENOW_PASSWORD")
TABLE = os.getenv("SERVICENOW_TABLE")

BASE_URL = f"https://{INSTANCE}/api/now/table/{TABLE}"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
