import argparse
from main import add_subscription, list_subscriptions, check_subscriptions, delete_subscription

def main():
    parser = argparse.ArgumentParser(description="Manage your subscriptions")
    parser.add_argument('-a', '--add', nargs=2, metavar=('NAME', 'EXPIRES'),
                        help="Add a new subscription with the format 'YYYY-MM-DD HH:MM'")
    parser.add_argument('-l', '--list', action='store_true', help="List all subscriptions")
    parser.add_argument('-d', '--delete', metavar='NAME', help="Delete a subscription by name")
    args = parser.parse_args()

    if args.add:
        name, expires = args.add
        add_subscription(name, expires)
        print(f"Added subscription for {name} expiring on {expires}.")
    elif args.list:
        list_subscriptions()
    elif args.delete:
        delete_subscription(args.delete)
    else:
        # Run a subscription check by default if no arguments are provided
        check_subscriptions()

if __name__ == "__main__":
    main()
