# Voice channel manager bot

This Discord bot allows users to create their own voice channel. The bot will automatically move the user to the new voice channel and give them management rights. If there are no users in the created channel after a minute, the bot will delete it.

## Features
- Create a voice channel: Users can create a new voice channel by joining the desired channel.
- Auto Move: After creating a new channel, the bot will automatically move the user into it.
- Permission Management: The user who created the channel will be given permissions to manage the channel.
- Auto purge: If there are no users left in the created voice channel after one minute, the bot will automatically delete it.

## Requirements
- Programming Language: Python
- Required Libraries: disnake (for interacting with Discord's API)
Install the required libraries using pip:
```
pip3 install disnake
```

## Setup
1. Create a bot on Discord:
- Go to the [Discord Developer Portal](https://discord.com/developers/).
- Create a new application, then create a bot and obtain the bot token.
- Replace the placeholder INSERT-TOKEN in the code with your bot token.
2. Configure the bot:
- Set the `voice_channel_id` list to include the IDs of the voice channels that will trigger the bot when a user joins.
- Set the `category_id` list to include the IDs of the categories where the new voice channels will be created.
3. Install Dependencies:
- On your machine, ensure Python 3.8+ is installed. You can check this by running:
```
python3 --version
```
- Install pip if it's not installed:
```
sudo apt install python3-pip
```
- Install the required libraries with pip:
```
pip3 install disnake
```
4. Run the bot:
- You can run the bot using the following command:
```
python3 app.py
```
Make sure you are in the same directory as the `app.py` file or provide the full path to it.

## How to Use
1. Deploy: Clone the repository and configure your bot.
2. Run: Launch the bot on your server.
3. Interaction: Once the bot is running, users will automatically have new voice channels created for them when they join a selected voice channel. After one minute of inactivity, the bot will automatically delete the channel.

## Links
[Boosty developer](https://boosty.to/mao-mao)

[GitHub](https://github.com/rinnyuwu)

[Donation Alerts](https://www.donationalerts.com/r/rinnyuwu)
