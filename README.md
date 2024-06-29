# Subscription Tracker

This Python project provides a simple tool to easily manage your subscription. It consists of two main scripts:
- `main.py`: Handles the logic for managing subscription data and sending notifications.
- `cli.py`: Provides a command-line interface to interact with the subscription management functions.

## Requirements
- Python 3.6 or higher
- macOS (due to the usage of AppleScript for notifications)

## Features
- **Add Subscriptions**: Allows users to add subscriptions with expiration dates.
- **Delete Subscriptions**: Allows users to delete an existing subscription.
- **List Subscriptions**: Displays all tracked subscriptions and their expiration dates.
- **Automatic Notifications**: Sends notifications when a subscription is about to expire (one day and two hours before the expiration).

## Setup
To run this project, follow these steps:

### Installation
1. **Clone the repository to where you want the project to stay:**
   ```bash
   git clone https://github.com/GhoulKingR/subscription-manager.git
   cd subscription-manager
   ```

2. **Ensure `osascript` is available:**
   This project uses AppleScript for sending notifications, which should be available by default on all macOS systems.

### Scheduling with `cron`
To automate the subscription checks, you can add a `cron` job that runs the script regularly:
1. Open the `cron` editor:
  ```bash
  crontab -e
  ```
2. Add a cron job to run the script every hour:
  ```cron
  0 * * * * /usr/bin/python3 /path/to/subscription-manager/main.py
  ```

### Configuration
No additional configuration is required.

## Usage
You can interact with the subscription tracker using the command-line interface provided by `cli.py`.

### Adding a Subscription
To add a new subscription, use the following command:
```bash
python3 cli.py --add "Service Name" "YYYY-MM-DD HH:MM"
```
Example:
```bash
python3 cli.py --add Netflix "2024-07-01 19:00"
```

### Deleting a Subscription
To delete an existing subscription, use the following command:
```bash
python cli.py --delete "Service Name"
```

Example:
```bash
python cli.py --delete "Netflix"
```

### Listing Subscriptions
To list all subscriptions, use:
```bash
python3 cli.py --list
```

### Automatic Checks
To check for expiring subscriptions and send notifications, you can run:
```bash
python3 cli.py
```
It's recommended to schedule this script to run at regular intervals using a scheduler like `cron` or `launchd`.

## Contribution
Contributions to this project are welcome. You can contribute by improving the scripts, adding new features, or reporting bugs.
