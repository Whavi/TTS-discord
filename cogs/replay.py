import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio


class Replay(commands.Cog):
    # Constructeur de la classe Replay
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="replay", description="Rejoue le dernier son TTS du bot")
    async def replay_slash(self, interaction: discord.Interaction):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du nom du salon vocal de l'utilisateur
        channel_name = user.voice.channel.name
        # Récupération de l'utilisateur si il est connecté
        voice_client = user.guild.voice_client

        if voice_client is not None:
            # Le bot est connecté dans un salon vocal
            vc = user.guild.voice_client
            source = FFmpegPCMAudio('audio.wav')  # Chemin vers le fichier audio à rejouer
            vc.play(source)  # Joue le fichier audio dans le salon vocal

            # Création d'un message embed pour afficher le résultat de l'action
            embed = discord.Embed(title="TTS replay",
                                  description="Le message a bien été renvoyé.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            # Affichage des informations de l'action dans la console
            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait un replay de l'audio 'audio.wav'")
            print("-------------------------------")

    @replay_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Replay(bot))
