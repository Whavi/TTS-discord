import discord
from discord.ext import commands
from discord import app_commands

class userInfo(commands.Cog):
    # Constructeur de la classe userInfo
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info_utilisateur", description="Donne les informations sur un utilisateur")
    async def userInfo_slash(self, interaction: discord.Interaction, membre: discord.Member):
        if membre is None:
            membre = interaction.user
        elif membre is not None:
            membre = membre

        membre_id = membre.id  # ID de l'utilisateur
        membre_name = membre.name  # Nom de l'utilisateur
        membre_nameServer = membre.display_name  # Nom de l'utilisateur sur le serveur
        membre_status = membre.status  # Statut de l'utilisateur
        membre_info_create = membre.created_at.strftime("%A %d %B %Y")  # Date de création de l'utilisateur

        embed = discord.Embed(title="Informations Utilisateur", color=0xff0000)
        embed.add_field(name="Pseudo :", value=membre_name, inline=False)
        embed.add_field(name="Pseudo Serveur :", value=membre_nameServer, inline=False)
        embed.add_field(name="ID :", value=membre_id, inline=False)
        embed.add_field(name="Statut :", value=membre_status, inline=False)
        embed.add_field(name="Créé depuis le :", value=membre_info_create, inline=False)

        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @userInfo_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions nécessaires.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(userInfo(bot))
