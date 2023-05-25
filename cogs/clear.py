import discord
from discord.ext import commands
from discord import app_commands
import asyncio


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Supprime le nombre de messages choisi")
    @app_commands.default_permissions(administrator=True)
    async def clear_slash(self, interaction: discord.Interaction, nombre: int, membre: discord.Member = None):
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du nom du salon vocal
        channel_name = interaction.channel.name
        # Récupération de l'instance de l'utilisateur
        user = interaction.user

        # Création de l'embed pour afficher le résultat du clear
        embed = discord.Embed(title="Clear",
                              description=f"Vous avez supprimé {nombre} message(s)",
                              color=0xff0000)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        # Envoi de l'embed en réponse à l'interaction
        await interaction.response.send_message(embed=embed, ephemeral=True)

        if not membre:
            # Suppression des messages sans filtrage par membre
            await interaction.channel.purge(limit=nombre)
            await asyncio.sleep(0.21)

        else:
            # Suppression des messages filtrés par membre
            await interaction.channel.purge(limit=nombre, check=lambda m: m.author == membre)
            await asyncio.sleep(0.21)

        # Affichage des informations du clear dans la console
        print(f"Server : {server_name}")
        print(f"Salon : {channel_name}")
        print(f"ID : {user.id}")
        print(f"{user.name} a clear {nombre} message")
        print("-------------------------------")

    @clear_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions pour pouvoir supprimer les messages", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Clear(bot))
