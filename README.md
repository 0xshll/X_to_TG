# Twitter to Telegram Monitor

Made by: @0xshll

---

## Introduction

This tool is a Python script designed to monitor Twitter accounts and send the latest tweets to a specified Telegram group. The tool includes an interactive interface for managing API keys and Telegram settings.

## Installation Requirements

Before starting, ensure you have the following Python libraries installed:

- tweepy: For interacting with the Twitter API.
- requests: For sending messages via Telegram.

You can install these libraries using:

pip install tweepy requests


## Setup

1. Twitter API Keys:
   - Obtain Twitter API keys from the Developer Portal.
   - Enter these keys into the script when selecting option 1 from the main menu.

2. Telegram Bot Token:
   - Create a Telegram bot using @BotFather and get the bot token.
   - Input the bot token when selecting option 2.

3. Twitter Accounts to Monitor:
   - Add the usernames you wish to monitor when selecting option 3. Enter each username on a new line, and type 'done' when finished.

4. Telegram User or Chat ID:
   - Enter the Telegram user or chat ID where you want to send messages when selecting option 4.

## How to Run

1. Welcome Screen:
   - Upon running the script, you'll see a welcome screen showing the developer (@yyeir).

2. Main Menu:
   - The main menu will display with the following options:
     - 1: Set Twitter API keys.
     - 2: Set Telegram bot token.
     - 3: Add Twitter usernames to monitor.
     - 4: Set Telegram chat username or ID.
     - 5: Clear saved sessions.
     - 6: Start monitoring.
     - 7: Exit.

3. Start Monitoring:
   - After setting up all requirements, select 6 to start monitoring. The script will begin monitoring for new tweets from the specified accounts and sending them to your Telegram group.

## Notes

- Authentication: Make sure you have proper authentication to use both Twitter and Telegram APIs.
- Rate Limits: Respect the rate limits of both APIs. You might encounter restrictions if limits are exceeded.
- Privacy: Use this tool with caution and respect for user privacy.

---

Important Note: Use this tool responsibly and in compliance with the terms of service for both Twitter and Telegram. The developer (@0xshll) is not responsible for any misuse of this tool.
