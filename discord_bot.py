import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO)
# Configure logging to both console and file
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
# Initialize an empty set for filtered words
filtered_words = set()

# Command to add a filtered word
@bot.command(name='addword')
async def add_word(ctx, word):
    filtered_words.add(word.lower())
    logging.info(f'Added filtered word "{word}" by {ctx.author.name}')
    await ctx.send(f'Added filtered word: "{word}"')
    

# Log errors
@bot.event
async def on_command_error(ctx, error):
    logging.error(f'Error in command {ctx.command}: {error}')

# Log when a message is deleted
@bot.event
async def on_message_delete(message):
    logging.info(f'Message deleted in {message.channel.name}: {message.content}')


@bot.command(name='clear')
async def clear(ctx, amount=5):
    # Command to clear a specified number of messages
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Cleared {amount} messages.', delete_after=5)

@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    # Command to ban a member from the server
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned. Reason: {reason}')

@bot.command(name='unban')
async def unban(ctx, *, member):
    # Command to unban a member
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}.')
            return

# Automod: Remove messages containing filtered words
@bot.event
async def on_message(message):
    for word in filtered_words:
        if word.lower() in message.content.lower():
            logging.info(f'Message containing filtered word "{word}" removed in {message.channel.name}: {message.content}')
            await message.delete()
            break  # Stop checking once a filtered word is found

    await bot.process_commands(message)
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


# React with 🗿 to every message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.add_reaction('🗿')

    # Spam prevention
    if len(message.content) > 100:  # Adjust the threshold as needed
        await message.channel.send(f"{message.author.mention}, please avoid spamming!")

    await bot.process_commands(message)


    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    # Command to check the bot's latency
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency is {latency}ms.')

@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    # Command to display user information
    member = member or ctx.author
    embed = discord.Embed(title=f'{member.name}#{member.discriminator}', color=member.color)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='ID', value=member.id, inline=False)
    embed.add_field(name='Joined Server', value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.add_field(name='Created Account', value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
