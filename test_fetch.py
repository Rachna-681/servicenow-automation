import requests
from requests.auth import HTTPBasicAuth
from config import BASE_URL, USER, PASSWORD, HEADERS

def fetch_one_task():
    query = {
        "sysparm_query": "state=6",  # Resolved tasks
        "sysparm_limit": "1"          # Only fetch 1 task for testing
    }
    
    try:
        response = requests.get(BASE_URL, auth=HTTPBasicAuth(USER, PASSWORD),
                                headers=HEADERS, params=query)
        response.raise_for_status()
        tasks = response.json().get("result", [])
        if tasks:
            task = tasks[0]
            print("✅ Successfully fetched a task:")
            print(f"Task Number: {task['number']}")
            print(f"Task State: {task['state']}")
            print(f"Sys ID: {task['sys_id']}")
        else:
            print("No tasks found matching the criteria.")
    except Exception as e:
        print(f"❌ Error fetching task: {e}")

if __name__ == "__main__":
    fetch_one_task()
