import discord
from discord import app_commands
from discord.ext import commands


class Join(commands.Cog):
    # Constructeur de la classe Join
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join", description="rejoint le salon auquel tu es connecté")
    async def join_slash(self, interaction: discord.Interaction,):

        user = interaction.user  # l'utilisateur
        server_name = interaction.guild.name  # le nom du serveur
        channel = interaction.user.voice.channel  # le salon vocal du serveur
        voice_client = interaction.guild.voice_client  # l'emplacement de l'utilisateur

        if voice_client is None:  # s'il n y a personne dans un salon vocal
            await channel.connect()  # alors il va se connecter au salon de l'utilisateur
        else:
            # sinon il va se connecter directement au salon de l'utilisateur
            await voice_client.move_to(channel)
        # embed de couleur rouge qui permet de dire que le bot est connecter
        embed = discord.Embed(title=" Connected",
                              description=f"Connecté au salon vocal {channel.name}",
                              color=0xff0000)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        print(f"Server : {server_name} ")
        print(f"Salon : {channel} ")
        print(f"ID : {user.id}")
        print(f"{user.name} a fait rejoindre le bot")

    @join_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Join(bot))
