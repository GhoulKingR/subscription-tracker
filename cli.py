import argparse
import subprocess
import requests
from main import add_subscription, list_subscriptions, check_subscriptions, delete_subscription

GITHUB_REPO_API_URL = 'https://api.github.com/repos/GhoulKingR/subscription-tracker/commits'

def get_local_version():
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_latest_commit():
    response = requests.get(GITHUB_REPO_API_URL)
    response.raise_for_status()
    commits = response.json()
    latest_commit = commits[0]
    return latest_commit['sha'], [commit['commit']['message'] for commit in commits]

def check_for_updates():
    local_version = get_local_version()
    latest_version, _ = get_latest_commit()
    return local_version != latest_version

def print_update_info():
    _, changelog = get_latest_commit()
    print("New version available 👨‍💻\n")
    print("Change Log:")
    for log in changelog:
        print(f" - {log}")

def update_application():
    subprocess.run(['git', 'pull'])
    print("Application updated to the latest version.")

def main():
    parser = argparse.ArgumentParser(description="Manage your subscriptions")
    parser.add_argument('-a', '--add', nargs=2, metavar=('NAME', 'EXPIRES'),
                        help="Add a new subscription with the format 'YYYY-MM-DD HH:MM'")
    parser.add_argument('-l', '--list', action='store_true', help="List all subscriptions")
    parser.add_argument('-d', '--delete', metavar='NAME', help="Delete a subscription by name")
    parser.add_argument('-u', '--update', action='store_true', help="Update the application to the latest version")
    parser.add_argument('-v', '--version', action='store_true', help="Check the current version and updates")
    args = parser.parse_args()

    if check_for_updates():
        print("New version available 👨‍💻\n")
        print("Run `python3 cli.py --version` for more information")

    if args.add:
        name, expires = args.add
        add_subscription(name, expires)
        print(f"Added subscription for {name} expiring on {expires}.")
    elif args.list:
        list_subscriptions()
    elif args.delete:
        delete_subscription(args.delete)
    elif args.update:
        update_application()
    elif args.version:
        if check_for_updates():
            print_update_info()
        else:
            print("Up to date ✅")
    else:
        # Run a subscription check by default if no arguments are provided
        check_subscriptions()

if __name__ == "__main__":
    main()
