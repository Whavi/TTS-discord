import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
import os
from discord.app_commands import Choice


choices_directory = "soundboard/"

selects = []

for filename in os.listdir(choices_directory):    
    name = os.path.splitext(filename)[0]  # Nom sans l'extension
    value = name.replace(" ", "_").replace("-", "_")# Remplace les espaces par des underscores
    os.rename(os.path.join(choices_directory, filename), os.path.join(choices_directory, value + ".wav"))
    select = Choice(name=name, value=value)
    selects.append(select)

# Renommer le fichier pour correspondre à la valeur

class Soundboard(commands.Cog):
    # Constructeur de la classe Join
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="soundboard", description="joue un soundboard qui est dans la base de donnée")
    @app_commands.choices(select=selects)
    async def Soundboard_slash(self, interaction: discord.Interaction, select: str):
        user = interaction.user
        server_name = interaction.guild.name
        channel_name = user.voice.channel.name
        voice_client = user.guild.voice_client

        if voice_client is not None:
            vc = user.guild.voice_client
            source = FFmpegPCMAudio(f'soundboard/{select}.wav')
            vc.play(source)

            embed = discord.Embed(title=" Soundboard jouer",
                                  description=f"Le soundboard à bien été jouer",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait un jouer de l'audio '{select}.wav'")
            print("-------------------------------")

    @Soundboard_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Soundboard(bot))
