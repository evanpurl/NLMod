import discord
from discord import app_commands
from discord.ext import commands
from util import accessutils


class messagetoannounce(discord.ui.Modal, title='NLS Owner Messaging System'):
    message = discord.ui.TextInput(label='Message', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.mention}, you submitted: Message: {self.message}')
        print(self)


# Needs "manage role" perms

class ownercommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="announce", description="Command used by the bot owner to announce things")
    async def announce(self, interaction: discord.Interaction) -> None:
        if str(interaction.user.id) in await accessutils.whohasaccess():
            # Bot would need to get all guilds from database, send message from guild id
            print(interaction)
            # NLAnnoucements category and channel
            # await interaction.response.send_modal(messagetoannounce())
        else:
            await interaction.response.send_message(content=f"You can't run this command", ephemeral=True)


async def setup(bot):
    await bot.add_cog(ownercommands(bot))
