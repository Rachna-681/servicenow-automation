import requests
from requests.auth import HTTPBasicAuth
import logging
from config import BASE_URL, USER, PASSWORD, HEADERS

# Setup logging
logging.basicConfig(
    filename="task_closer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_tasks():
    """Fetch tasks that are resolved for more than 3 days"""
    query = {
        "sysparm_query": "state=6^resolved_atRELATIVELE@dayofweek@ago@3",
        "sysparm_limit": "10"
    }
    try:
        response = requests.get(BASE_URL, auth=HTTPBasicAuth(USER, PASSWORD),
                                headers=HEADERS, params=query)
        response.raise_for_status()
        return response.json().get("result", [])
    except Exception as e:
        logging.error(f"Error fetching tasks: {e}")
        return []

def close_task(task):
    """Close a single task"""
    task_id = task["sys_id"]
    task_number = task["number"]
    update_url = f"{BASE_URL}/{task_id}"
    
    payload = {
        "state": "7",  # Closed
        "close_notes": "Closed automatically by Python script"
    }
    
    try:
        resp = requests.patch(update_url, auth=HTTPBasicAuth(USER, PASSWORD),
                              headers=HEADERS, json=payload)
        if resp.status_code == 200:
            logging.info(f"Closed task {task_number}")
            print(f"✅ Closed task {task_number}")
        else:
            logging.error(f"Failed to close {task_number}: {resp.text}")
            print(f"❌ Failed to close {task_number}")
    except Exception as e:
        logging.error(f"Error closing {task_number}: {e}")

def main():
    tasks = fetch_tasks()
    if not tasks:
        print("No tasks to close.")
        return
    
    for task in tasks:
        close_task(task)

if __name__ == "__main__":
    main()
