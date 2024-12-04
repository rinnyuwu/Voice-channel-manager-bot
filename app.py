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

voice_channel_ids = [123456789, 123456789]  # Replace with the desired voice channel ID
category_ids = [123456789, 123456789]  # Replace with the desired category ID


@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id in voice_channel_ids:
        categories = [category for category in member.guild.categories if category.id in category_ids]

        if not categories:
            return

        chosen_category = random.choice(categories)

        new_voice_channel = await member.guild.create_voice_channel(
            name=f"{member.name}'s Channel", category=chosen_category
        )

        await member.move_to(new_voice_channel)

        await new_voice_channel.set_permissions(
            member, manage_channels=True, connect=True, speak=True
        )

        await check_and_delete_channel(new_voice_channel)

async def check_and_delete_channel(channel: disnake.VoiceChannel):
    await asyncio.sleep(60)

    if channel.guild.get_channel(channel.id) is None:
        return

    if len(channel.members) == 0:
        await channel.delete()

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources
