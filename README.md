# Your Bot Name

Brief description of your bot.

## Table of Contents
- [Features](#features)
- [Commands](#commands)
- [Setup](#setup)
- [Dependencies](#dependencies)
- [License](#license)

## Features
- Reacts with 🗿 to every message.
- Automatic message deletion for filtered words.
- Welcome message for new members.
- Clear command to remove messages.
- Ban and unban commands.
- Customizable filtered word list.
- Logging of deleted messages and errors.
- User information display command.
- Ping command to check bot latency.

## Commands
- `!ping`: Check the bot's latency.
- `!userinfo [member]`: Display user information.
- `!addword [word]`: Add a filtered word.
- `!clear [amount]`: Clear a specified number of messages.
- `!ban [member] [reason]`: Ban a member with an optional reason.
- `!unban [member]`: Unban a member.
- ... (Add more commands as needed)

## Setup
1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/your-bot.git
   cd your-bot
   ```
2. Install dependencies.
       ```bash
       pip install -r requirements.txt
        ```
3. Create a config.py file and add your Discord bot token.
       ```python
       # config.py
        TOKEN = 'your_bot_token_here'
        ```
   4. Run the bot.
           ```python
          python bot.py
          ```
   # Dependencies
   * discord.py
   * logging
   # License
   This project is licensed under the [MIT license](https://github.com/Taoballl/moai-reactor/blob/main/LICENSE) - see the [LICENSE.md](https://github.com/Taoballl/moai-reactor/blob/main/LICENSE) file for details.
