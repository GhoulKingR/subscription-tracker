import datetime
import json
import subprocess
from pathlib import Path
import os

def send_notification(title, message):
    apple_script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", apple_script])

def load_subscriptions():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    subs_file = Path(os.path.join(current_directory, "subscriptions.json"))
    if not subs_file.exists():
        return {}
    with open(subs_file, 'r') as file:
        return json.load(file)

def save_subscriptions(subscriptions):
    with open("subscriptions.json", 'w') as file:
        json.dump(subscriptions, file, indent=4)

def check_subscriptions():
    subscriptions = load_subscriptions()
    now = datetime.datetime.now()
    for sub, info in subscriptions.items():
        exp_date = datetime.datetime.strptime(info['expires'], '%Y-%m-%d %H:%M')
        time_diff = exp_date - now
        if time_diff.days == 0 and time_diff.seconds <= 7200:  # 2 hours before
            send_notification("Subscription Alert", f"{sub} is expiring in less than 2 hours!")
        elif time_diff.days == 1:
            send_notification("Subscription Alert", f"{sub} is expiring tomorrow!")

def add_subscription(name, expires):
    subscriptions = load_subscriptions()
    subscriptions[name] = {'expires': expires}
    save_subscriptions(subscriptions)

def list_subscriptions():
    subscriptions = load_subscriptions()
    if not subscriptions:
        print("No subscriptions found.")
    for sub, info in subscriptions.items():
        print(f"{sub}: expires on {info['expires']}")

def delete_subscription(name):
    subscriptions = load_subscriptions()
    if name in subscriptions:
        del subscriptions[name]
        save_subscriptions(subscriptions)
        print(f"Subscription for {name} has been deleted.")
    else:
        print(f"No subscription found for {name}.")

# Example to add a new subscription
# add_subscription("Netflix", "2024-07-01 19:00")

# Regularly check subscriptions
if __name__ == "__main__":
    check_subscriptions()
