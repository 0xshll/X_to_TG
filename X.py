import os
import time
import json
import tweepy
import requests

# Print banner function
def print_banner():
    os.system("clear" if os.name == "posix" else "cls")
    banner = """
╔════════════════════════════════════════════╗
║                                            ║
║        Made with 💻 by Yasser              ║
║        Telegram: @yyeir                   ║
║                                            ║
╚════════════════════════════════════════════╝
"""
    print(banner.center(80))

# Print banner at the top
print_banner()

SESSION_FILE = "session.json"
USERS_FILE = "twitter_users.txt"

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_session(data):
    with open(SESSION_FILE, 'w') as f:
        json.dump(data, f)

def delete_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    if os.path.exists(USERS_FILE):
        os.remove(USERS_FILE)

def send_telegram_message(bot_token, chat_username, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_username,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"[!] Failed to send Telegram message: {response.text}")
    except Exception as e:
        print(f"[!] Telegram Error: {e}")

def monitor_twitter(twitter_api, usernames, telegram_bot_token, telegram_chat_id):
    print("[*] Monitoring Twitter accounts...")
    last_seen = {}
    while True:
        for username in usernames:
            try:
                user = twitter_api.get_user(screen_name=username)
                tweets = twitter_api.user_timeline(user_id=user.id, count=1, tweet_mode="extended")
                if tweets:
                    tweet = tweets[0]
                    if username not in last_seen or tweet.id != last_seen[username]:
                        message = f"📢 <b>New tweet from @{username}</b>:\n\n{tweet.full_text}"
                        send_telegram_message(telegram_bot_token, telegram_chat_id, message)
                        last_seen[username] = tweet.id
            except Exception as e:
                print(f"[!] Error with @{username}: {e}")
        time.sleep(3)

def print_menu():
    print("\n=== Twitter to Telegram Monitor ===")
    print("1. Set Twitter API keys")
    print("2. Set Telegram bot token")
    print("3. Add Twitter usernames to monitor")
    print("4. Set Telegram chat username or ID")
    print("5. Clear saved sessions")
    print("6. Start monitoring")
    print("7. Exit")

def main():
    session = load_session()

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            api_key = input("Twitter API Key: ")
            api_secret = input("Twitter API Secret: ")
            access_token = input("Twitter Access Token: ")
            access_token_secret = input("Twitter Access Token Secret: ")
            session["twitter"] = {
                "api_key": api_key,
                "api_secret": api_secret,
                "access_token": access_token,
                "access_token_secret": access_token_secret
            }
            save_session(session)
            print("[+] Twitter API credentials saved.")

        elif choice == "2":
            bot_token = input("Telegram Bot Token: ")
            session.setdefault("telegram", {})["bot_token"] = bot_token
            save_session(session)
            print("[+] Telegram bot token saved.")

        elif choice == "3":
            print("Enter Twitter usernames (without @), one per line. Type 'done' when finished:")
            usernames = []
            while True:
                u = input("> ")
                if u.lower() == 'done':
                    break
                usernames.append(u.strip())
            with open(USERS_FILE, 'w') as f:
                for u in usernames:
                    f.write(u + "\n")
            print("[+] Twitter usernames saved.")

        elif choice == "4":
            chat_id = input("Telegram chat username or ID: ")
            session.setdefault("telegram", {})["chat_id"] = chat_id
            save_session(session)
            print("[+] Telegram chat ID saved.")

        elif choice == "5":
            delete_session()
            print("[+] Sessions cleared.")

        elif choice == "6":
            if "twitter" not in session or "telegram" not in session:
                print("[!] Twitter and Telegram credentials must be set first.")
                continue
            if not os.path.exists(USERS_FILE):
                print("[!] No Twitter usernames found. Add them first.")
                continue
            with open(USERS_FILE) as f:
                usernames = [line.strip() for line in f if line.strip()]
            try:
                auth = tweepy.OAuth1UserHandler(
                    session["twitter"]["api_key"],
                    session["twitter"]["api_secret"],
                    session["twitter"]["access_token"],
                    session["twitter"]["access_token_secret"]
                )
                api = tweepy.API(auth)
                monitor_twitter(api, usernames, session["telegram"]["bot_token"], session["telegram"]["chat_id"])
            except Exception as e:
                print(f"[!] Failed to start monitoring: {e}")

        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
