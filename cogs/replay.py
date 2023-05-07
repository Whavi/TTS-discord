import discord
import os
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
from gtts import gTTS


class Replay(commands.Cog):
    # Constructeur de la classe Join
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="replay", description="rejoue le dernier son tts du bot")
    async def replay_slash(self, interaction: discord.Interaction):
        user = interaction.user
        server_name = interaction.guild.name
        channel_name = user.voice.channel.name
        voice_client = interaction.guild.voice_client

        if user.voice is not None:
            vc = interaction.voice_client
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
            embed = discord.Embed(title=" TTS replay",
                                  description=f"Le message à bien été renvoyer",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait un replay de l'audio 'audio.wav'")

    @replay_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Replay(bot))
