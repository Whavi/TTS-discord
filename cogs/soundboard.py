import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
import os
from discord.app_commands import Choice

choices_directory = "soundboard/"

selects = []

# Parcours des fichiers dans le répertoire soundboard
for filename in os.listdir(choices_directory):
    name = os.path.splitext(filename)[0]  # Nom sans l'extension
    # Remplace les tirets et underscores par des espaces dans le nom
    value = name.replace("-", " ").replace("_", " ")
    os.rename(os.path.join(choices_directory, filename),
              os.path.join(choices_directory, value + ".wav"))  # Renomme le fichier pour correspondre à la valeur
    select = Choice(name=name, value=value)  # Crée un objet Choice pour les options de la commande
    selects.append(select)  # Ajoute l'option à la liste des options disponibles

class Soundboard(commands.Cog):
    # Constructeur de la classe Soundboard
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="soundboard", description="Joue un son du soundboard")
    @app_commands.choices(select=selects)  # Définition des options pour la commande soundboard
    async def Soundboard_slash(self, interaction: discord.Interaction, select: str):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du nom du salon vocal de l'utilisateur
        channel_name = user.voice.channel.name
        # Récupération de l'utilisateur si il est connecté
        voice_client = user.guild.voice_client

        if voice_client is not None:
            vc = user.guild.voice_client
            try:
                source = FFmpegPCMAudio(f'soundboard/{select}.wav')  # Chargement du fichier audio à jouer
            except FileNotFoundError:
                print(f"File not found: {select}.wav")
                return

            vc.play(source)  # Joue le fichier audio dans le salon vocal

            embed = discord.Embed(title="Soundboard jouer",
                                  description="Le soundboard a bien été joué.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a joué l'audio '{select}.wav' depuis le soundboard")
            print("-------------------------------")

    @Soundboard_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Soundboard(bot))
