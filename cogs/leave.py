import discord
from discord import app_commands
from discord.ext import commands


class Leave(commands.Cog):
    # Constructeur de la classe leave
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leave", description="déconnecte le bot du salon auquel tu es connecté")
    async def leave_slash(self, interaction: discord.Interaction):
        server_name = interaction.guild.name  # le nom du serveur
        channel = interaction.user.voice.channel  # le salon du serveur
        voice_client = interaction.guild.voice_client  # l'emplacement de l'utilisateur

        if channel is None:
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)
            return

        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
            await voice_client.disconnect()
            await print(f"Déconnecté du salon vocal {channel.name} dans le serveur de {server_name}.")
            embed = discord.Embed(title=" Connected",
                                  description=f"Connecté au salon vocal {channel.name}",
                                  color=0xff0000)
            embed.set_footer(text="Bot fait par Fethi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @leave_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Leave(bot))
