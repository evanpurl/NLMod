import discord
from discord import app_commands
from discord.ext import commands
from util import accessutils


# Needs "manage role" perms

class ownercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Command used by the bot owner to announce things")
    async def announce(self, interaction: discord.Interaction) -> None:
        if str(interaction.user.id) in await accessutils.whohasaccess():
            # NLAnnoucements category and channel
            # await interaction.response.send_modal(classCreation())
            await interaction.response.send_message(content=f"This will do something", ephemeral=True)
        else:
            await interaction.response.send_message(content=f"You can't run this command", ephemeral=True)


async def setup(bot):
    await bot.add_cog(ownercommands(bot))
