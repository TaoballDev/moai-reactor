import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_member_join(member):
    # Send a welcome message when a new member joins
    welcome_channel = member.guild.system_channel
    if welcome_channel:
        welcome_message = f"Welcome to 🗿, {member.mention}! Make sure to read the rules in #welcome 🗿."
        await welcome_channel.send(welcome_message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # React with 🗿 to every message
    await message.add_reaction('🗿')

    # Spam prevention
    if len(message.content) > 100:  # Adjust the threshold as needed
        await message.channel.send(f"{message.author.mention}, please avoid spamming!")

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
