import discord
from discord import app_commands
from discord.ext import commands
from util import accessutils


# Needs "manage role" perms

class admincommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="warn", description="Command used by a moderator or admin to warn people.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def warn(self, interaction: discord.Interaction, user: discord.User, reason: str) -> None:
        msg = f"""You have been warned on __{interaction.guild.name}__ for reason **{reason}**. Please contact an 
admin if you have any questions. """
        await user.send(msg)
        await interaction.response.send_message(content=f"Warning sent to user __{user.name}__ for reason **{reason}**", ephemeral=True)

    @app_commands.command(name="verifyfor", description="Command used by an admin to add user to the Verified role")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def verifyfor(self, interaction: discord.Interaction, user: discord.User) -> None:
        role = discord.utils.get(interaction.guild.roles, name="Verified")
        if role:
            if role in user.roles:
                await interaction.response.send_message(f"User has already been verified.", ephemeral=True)
            else:
                oldrole = discord.utils.get(interaction.guild.roles, name="Unverified")
                await user.add_roles(role)
                await user.remove_roles(oldrole)
                await interaction.response.send_message(f"User has been added to the Verified role.", ephemeral=True)
        else:
            await interaction.guild.create_role(name="Verified")
            role = discord.utils.get(interaction.guild.roles, name="Verified")
            oldrole = discord.utils.get(interaction.guild.roles, name="Unverified")
            await user.add_roles(role)
            await user.remove_roles(oldrole)
            await interaction.response.send_message(f"User has been added to the Verified role.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(admincommands(bot))
