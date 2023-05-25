import discord
from discord import app_commands
from discord.ext import commands


class Leave(commands.Cog):
    # Constructeur de la classe Leave
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leave", description="Déconnecte le bot du salon auquel tu es connecté")
    async def leave_slash(self, interaction: discord.Interaction):
        user = interaction.user  # L'utilisateur
        server_name = interaction.guild.name  # Le nom du serveur
        channel = interaction.user.voice.channel  # Le salon vocal du serveur
        voice_client = interaction.guild.voice_client  # L'emplacement du bot

        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
            await voice_client.disconnect()

            # Création de l'embed pour afficher le message de déconnexion
            embed = discord.Embed(title="Disconnected",
                                  description=f"Déconnecté du salon vocal {channel.name}",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")

            # Envoi de l'embed en réponse à l'interaction (message éphémère)
            await interaction.response.send_message(embed=embed, ephemeral=True)

            # Affichage des informations de déconnexion dans la console
            print(f"Server : {server_name} ")
            print(f"Salon : {channel} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait déconnecté le bot")
            print("-------------------------------")

    @leave_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Leave(bot))
