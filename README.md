# Discord.py Demo Bot

Welcome to the **Discord.py Demo Bot**! 🚀

This repository is designed to be the perfect starting point for **absolute beginners** who want to learn how to create Discord bots using Python and the `discord.py` library.

It includes everything you need to understand the basics:
*   **Slash Commands** (the modern way to interact with bots).
*   **Events** (how the bot reacts to messages, startup, etc.).
*   **Cogs** (how to organize your code into multiple files).
*   **Interactive UI** (Buttons, Select Menus).

---

## 📚 Prerequisites

Before you start, you need a few tools installed on your computer:

1.  **Python**: The programming language we are using.
    *   Download and install **Python 3.10 or newer** from [python.org](https://www.python.org/downloads/).
    *   *Important*: During installation, check the box that says **"Add Python to PATH"**.

2.  **Code Editor**: A place to write and read your code.
    *   We recommend [Visual Studio Code (VS Code)](https://code.visualstudio.com/), which is free and beginner-friendly.

3.  **Git** (Optional but recommended): Helps you download this project easily.
    *   Download from [git-scm.com](https://git-scm.com/downloads).

---

## 🛠️ Setup Guide

Follow these steps carefully to get your bot running!

### 1. Create a Discord Application
1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Click **"New Application"**, give it a name (e.g., "MyFirstBot"), and create it.
3.  Go to the **"Bot"** tab on the left sidebar.
4.  Click **"Add Bot"** and confirm.
5.  **Important**: Scroll down to the **"Privileged Gateway Intents"** section.
    *   Enable **Presence Intent**.
    *   Enable **Server Members Intent**.
    *   Enable **Message Content Intent**.
    *   *Why?* These allow your bot to see who is in the server and read command messages.
6.  Click **"Save Changes"**.
7.  Scroll back up to the **"Token"** section. Click **"Reset Token"**, then **"Copy"**.
    *   *Warning*: **Never share this token!** It is your bot's password.

### 2. Invite the Bot to Your Server
1.  Go to the **"OAuth2"** tab -> **"URL Generator"**.
2.  Under **Scopes**, check `bot` and `applications.commands`.
3.  Under **Bot Permissions**, check `Administrator` (for testing purposes; later you can be more specific).
4.  Copy the generated URL at the bottom and paste it into your browser to invite the bot to your test server.

### 3. Download the Code
If you have Git installed, open your terminal (Command Prompt or PowerShell) and run:
```bash
git clone https://github.com/Xougui/demobot.git
cd demobot
```
*Alternatively, you can click the green "Code" button on GitHub and select "Download ZIP", then extract it.*

### 4. Install Dependencies
In your terminal (inside the `demobot` folder), run:
```bash
pip install -r requirements.txt
```
*Note: On macOS/Linux, you might need to use `pip3` instead of `pip`.*

### 5. Configure Your Bot
1.  Find the file named `.env.example`.
2.  Rename it to `.env`.
3.  Open `.env` with your text editor.
4.  Paste your copied Bot Token after `DISCORD_TOKEN=`.
5.  (Optional) Paste your User ID after `OWNER_ID=` (Enable "Developer Mode" in Discord settings to right-click your profile and "Copy ID").
6.  (Optional) Fill in `LOG_CHANNEL_ID` and `LOG_SERVER_ID` if you want to test logging features.

Your `.env` file should look something like this:
```env
DISCORD_TOKEN=MTAw... (your long token here)
OWNER_ID=123456789...
...
```

### 6. Run the Bot!
In your terminal, run:
```bash
python main.py
```
*Note: On macOS/Linux, you might need `python3 main.py`.*

If successful, you should see:
```
Bot is ready.
Bot running with:
Username:  MyFirstBot#1234
User ID:  ...
Synced 8 commands
```

---

## 🎮 Commands

Go to your Discord server and type `/` to see the available commands!

### General
*   `/ping`: Check if the bot is alive. It responds with "Pong!".
*   `!create_invite`: Creates an invite link (needs 'Manage Server' permission).

### Fun & UI Examples
*   `/buttons`: Shows buttons you can click.
*   `/select_menu`: Shows a dropdown menu.
*   `/counter`: Starts a counting game in a specific channel.
*   `/testbutton`: A button that still works even if you restart the bot!

### Admin
*   `/dm [member] [message]`: Sends a private message to a user as the bot.

---

## 📂 Project Structure (How it works)

*   `main.py`: The **brain** of the bot. It starts the bot, loads extensions, and handles basic startup tasks.
*   `cog/`: This folder contains **Extensions** (or "Cogs"). Think of them as plugins or modules.
    *   `dm.py`: Handles the `/dm` command.
    *   `example_cog.py`: A very simple example to copy when making your own commands.
    *   `logging.py`: Shows how to log events.
    *   `button.py` / `selector.py`: Examples of interactive buttons and menus.
*   `data/`: Where the bot saves data (like the counting game score).
*   `.env`: Your secrets (Token). **Git ignores this file so your token doesn't get leaked.**

---

## ❓ Troubleshooting

*   **"ModuleNotFoundError"**: You forgot to run `pip install -r requirements.txt`.
*   **"LoginFailure: Improper token"**: Your token in the `.env` file is wrong. Make sure you copied it correctly.
*   **"Privileged Intents... are not enabled"**: You missed step 1.5 in the setup guide. Go to the Developer Portal and enable the Intents.
*   **Commands don't show up**: Wait a minute or restart your Discord app (Ctrl+R). Slash commands sometimes take time to appear.

---

Happy Coding! 🎉
