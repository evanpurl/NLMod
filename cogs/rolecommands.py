import discord
from discord import app_commands
from discord.ext import commands


# Needs "manage role" perms

class rolecommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="gender", description="Command used to assign someone to a role for their gender.")
    @app_commands.choices(genders=[
        app_commands.Choice(name='Male', value=1),
        app_commands.Choice(name='Female', value=2),
        app_commands.Choice(name='Non-Binary', value=3),
        app_commands.Choice(name='Something Else', value=4),
    ])
    async def gender(self, interaction: discord.Interaction, genders: app_commands.Choice[int]) -> None:
        role = discord.utils.get(interaction.guild.roles, name=genders.name)
        if not role:
            await interaction.guild.create_role(name=genders.name)
        role = discord.utils.get(interaction.guild.roles, name=genders.name)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been added to the {genders.name} role.", ephemeral=True)
        else:
            await interaction.response.send_message(f"This bot cannot run this function at this time.", ephemeral=True)

    @app_commands.command(name="pronouns", description="Command used to assign someone to a role for their pronouns.")
    @app_commands.choices(pronouns=[
        app_commands.Choice(name='He/Him', value=1),
        app_commands.Choice(name='She/Her', value=2),
        app_commands.Choice(name='They/Them', value=3),
        app_commands.Choice(name='Something Else', value=4),
    ])
    async def pronouns(self, interaction: discord.Interaction, pronouns: app_commands.Choice[int]) -> None:
        role = discord.utils.get(interaction.guild.roles, name=pronouns.name)
        if not role:
            await interaction.guild.create_role(name=pronouns.name)
        role = discord.utils.get(interaction.guild.roles, name=pronouns.name)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been added to the {pronouns.name} role.", ephemeral=True)
        else:
            await interaction.response.send_message(f"This bot cannot run this function at this time.", ephemeral=True)

    @app_commands.command(name="verify", description="Command used to add user to the Verified role")
    async def verify(self, interaction: discord.Interaction) -> None:
        role = discord.utils.get(interaction.guild.roles, name="Verified")
        if role:
            if role in interaction.user.roles:
                await interaction.response.send_message(f"You have already been verified.", ephemeral=True)
            else:
                oldrole = discord.utils.get(interaction.guild.roles, name="Unverified")
                await interaction.user.add_roles(role)
                await interaction.user.remove_roles(oldrole)
                await interaction.response.send_message(f"You have been added to the Verified role.", ephemeral=True)
        else:
            await interaction.guild.create_role(name="Verified")
            role = discord.utils.get(interaction.guild.roles, name="Verified")
            oldrole = discord.utils.get(interaction.guild.roles, name="Unverified")
            await interaction.user.add_roles(role)
            await interaction.user.remove_roles(oldrole)
            await interaction.response.send_message(f"You have been added to the Verified role.", ephemeral=True)

    @app_commands.command(name="unverify", description="Admin command to unverify people.")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def unverify(self, interaction: discord.Interaction, user: discord.User) -> None:
        role = discord.utils.get(interaction.guild.roles, name="Unverify")
        if role:
            if role in user.roles:
                await interaction.response.send_message(f"User is already unverified.", ephemeral=True)
            else:
                oldrole = discord.utils.get(interaction.guild.roles, name="Verified")
                await user.add_roles(role)
                await user.remove_roles(oldrole)
                await interaction.response.send_message(f"User has been unverified.", ephemeral=True)
        else:
            await interaction.guild.create_role(name="Unverified")
            role = discord.utils.get(interaction.guild.roles, name="Unverified")
            oldrole = discord.utils.get(interaction.guild.roles, name="Verified")
            await user.add_roles(role)
            await user.remove_roles(oldrole)
            await interaction.response.send_message(f"User has been unverified.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(rolecommands(bot))
