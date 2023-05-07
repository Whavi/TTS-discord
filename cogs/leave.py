import discord
from discord import app_commands
from discord.ext import commands


class Leave(commands.Cog):
    # Constructeur de la classe leave
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leave", description="déconnecte le bot du salon auquel tu es connecté")
    async def leave_slash(self, interaction: discord.Interaction):
        user = interaction.user  # l'utilisateur
        server_name = interaction.guild.name  # le nom du serveur
        channel = interaction.user.voice.channel  # le salon du serveur
        voice_client = interaction.guild.voice_client  # l'emplacement de l'utilisateur

        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
            await voice_client.disconnect()

            embed = discord.Embed(title=" Disconnected",
                                  description=f"Deconnecté du salon vocal {channel.name}",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            print(f"Server : {server_name} ")
            print(f"Salon : {channel} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait déconnecté le bot")

    @leave_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Leave(bot))
