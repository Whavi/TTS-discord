import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
import os
from discord.app_commands import Choice

choices_directory = "music/"

selects = []

# Parcourir les fichiers dans le répertoire "music/"
for filename in os.listdir(choices_directory):
    name = os.path.splitext(filename)[0]  # Nom sans l'extension
    # Remplace les espaces par des underscores
    value = name.replace("-", " ").replace("_", " ")
    # Renommer le fichier pour correspondre à la valeur
    os.rename(os.path.join(choices_directory, filename),
              os.path.join(choices_directory, value + ".wav"))
    # Créer un objet Choice avec le nom et la valeur
    select = Choice(name=name, value=value)
    selects.append(select)

class music(commands.Cog):
    # Constructeur de la classe music
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="music", description="Joue une musique qui est dans la base de données")
    @app_commands.choices(select=selects)  # Ajouter les choix à la commande
    async def music_slash(self, interaction: discord.Interaction, select: str):
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
                # Charger le fichier audio avec FFmpegPCMAudio
                source = FFmpegPCMAudio(f'music/{select}.wav')
            except FileNotFoundError:
                print(f"Fichier non trouvé: {select}.wav")
                return

        if vc.is_playing():
            # Embed pour indiquer qu'une musique est déjà en cours de lecture
            embed = discord.Embed(title="Musique en cours",
                                  description="Une musique est déjà en train d'être jouée, veuillez attendre la fin de celle-ci.",
                                  color=0xff0000)
        else:
            vc.play(source)
            # Embed pour indiquer que la musique a été jouée
            embed = discord.Embed(title="Musique jouée",
                                  description="La musique a bien été jouée.",
                                  color=0xff0000)

        embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

        print(f"Server : {server_name} ")
        print(f"Salon : {channel_name} ")
        print(f"ID : {user.id}")
        print(f"{user.name} a joué la musique '{select}.wav'")
        print("-------------------------------")

    @music_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(music(bot))
