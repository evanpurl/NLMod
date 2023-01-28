import asyncio
import discord
from discord.ext import commands
import os
from util.accessutils import whohasaccess

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)


# No longer syncs in on_ready, if new commands are added, run $reloadcogs
@client.event
async def on_ready():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name=f"Powered by Nite Life Software"))
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f"This will be different in the future :) {member.mention}")
    role = discord.utils.get(member.guild.roles, name="Unverified")
    if role:
        await member.add_roles(role)
    else:
        pass


@client.event
async def on_guild_join(guild):
    category = await discord.utils.get(guild.categories, name="NLAnnouncements")
    if category:
        channel = await discord.utils.get(guild.channels, name="NLAnnouncements")
        if not channel:
            channel = await guild.create_text_channel('NLAnnouncements', category=category)
        await channel.send("NLMod has been installed!")
    else:
        category = await guild.create_category("NLAnnouncements")
        channel = await discord.utils.get(guild.channels, name="NLAnnouncements")
        if not channel:
            channel = await guild.create_text_channel('NLAnnouncements', category=category)
        await channel.send("NLMod has been installed!")


# reloadcogs command is used to reload all cogs.
@client.command(name="reloadcogs", description="command to reload cogs")
async def reload(ctx) -> None:
    if str(ctx.message.author.id) in await whohasaccess():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await ctx.send(f"reloading cog: {filename[:-3]}")
                await client.reload_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"Syncing commands")
        await client.tree.sync()
        await ctx.send(f"Commands synced")
    else:
        await ctx.send(f"You can't run this command.")


# Function used to load extensions into the bot
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f"Loading cog: {filename[:-3]}")
            await client.load_extension(f"cogs.{filename[:-3]}")


# Main function to load extensions and then load bot.
async def main():
    async with client:
        try:
            with open('token/token.txt', 'r') as token:
                token = token.read()
            await load_extensions()
            await client.start(token)
        except KeyboardInterrupt:
            pass


asyncio.run(main())  # Runs main function above
