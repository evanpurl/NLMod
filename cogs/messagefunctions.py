import discord
from discord.ext import commands


class messagefunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if len(message.content) <= 1500:
            print(f"Message from {message.author.name} in channel {message.channel.mention} deleted: {message.content}")
        else:
            print(
                f"Message from {message.author.name} in channel {message.channel.mention} deleted: content too long to send.")

    @commands.Cog.listener()
    async def on_message_edit(self, message_before: discord.Message, message_after: discord.Message):
        msgsum = sum([len(message_before.content), len(message_after.content)])
        if msgsum <= 1500:
            print(f"Message from {message_before.author.name} in channel {message_before.channel.mention} edited from {message_before.content} to {message_after.content}")
        else:
            print(
                f"Message from {message_before.author.name} in channel {message_before.channel.mention} edited: content too long to send.")


async def setup(bot: commands.Cog):
    await bot.add_cog(messagefunctions(bot))
