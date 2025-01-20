import disnake
from disnake.ext import commands, tasks
import random
import asyncio

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

voice_channel_id = [123456789, 123456789]  # Replace with the desired voice channel ID
category_id = [123456789, 123456789]  # Replace with the desired category ID
created_channels = set()

@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")
    check_empty_channels.start()

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id in voice_channel_id:
        categories = [category for category in member.guild.categories if category.id in category_id]

        if not categories:
            return

        chosen_category = random.choice(categories)

        new_voice_channel = await member.guild.create_voice_channel(
            name=f"{member.name}'s Channel", category=chosen_category
        )

        created_channels.add(new_voice_channel.id)

        await member.move_to(new_voice_channel)

        await new_voice_channel.set_permissions(
            member, manage_channels=True, connect=True, speak=True
        )

@tasks.loop(seconds=60)
async def check_empty_channels():
    for channel_id in list(created_channels):
        channel = bot.get_channel(channel_id)
        if channel and len(channel.members) == 0:
            await channel.delete()
            created_channels.remove(channel_id)

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources
