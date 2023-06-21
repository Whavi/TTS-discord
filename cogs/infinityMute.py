import asyncio
import discord
from discord.ext import commands
from discord import app_commands


class muteInfinity(commands.Cog):
    # Constructeur de la classe muteDefean
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mute_infinity", description="Mute le casque de façon permanente pour la personne choisie sans possibilité de retour en arrière")
    # Seulement les administrateurs peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def muteInfinity_slash(self, interaction: discord.Interaction, membre: discord.Member):
        users = interaction.user  # L'utilisateur qui a déclenché la commande
        server_name = interaction.guild.name  # Le nom du serveur
        voice_client_membre = membre.voice

        if not voice_client_membre:
            # L'utilisateur n'est pas connecté dans un salon vocal
            embed = discord.Embed(title="Mute Casque",
                                  description=f"{membre.display_name} n'est pas connecté dans un salon vocal.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else: 
            while True:
                await membre.edit(mute=True, deafen=True) # Activer ou désactiver le mute du casque et du micro 
                await asyncio.sleep(1)
            
        print(f"Server : {server_name} ")
        print(f"ID user : {users.id}")
        print(
            f"La personne {membre.name} a été rendue sourde à vie dans le salon vocal par {users.name}#{users.discriminator} | {users.display_name}")
        print("-------------------------------")
        
        


    @muteInfinity_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions")


async def setup(bot):
    await bot.add_cog(muteInfinity(bot))
