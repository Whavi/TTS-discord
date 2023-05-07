import discord
from discord import app_commands
from discord.ext import commands


class Join(commands.Cog):
    # Constructeur de la classe Join
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join", description="rejoint le salon auquel tu es connecté")
    async def join_slash(self, interaction: discord.Interaction):

        server_name = interaction.guild.name  # le nom du serveur
        channel = interaction.user.voice.channel  # le salon du serveur
        voice_client = interaction.guild.voice_client  # l'emplacement de l'utilisateur

        if voice_client is None:  # s'il n y a personne dans un salon
            await channel.connect()  # alors il va se connecter au salon de l'utilisateur
        else:
            # sinon il va se connecter directement au salon de l'utilisateur
            await voice_client.move_to(channel)
            print(
                f"Connecté au salon vocal {channel.name} dans le serveur de {server_name} !")

    @join_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        channel = interaction.user.voice.channel
        if channel is None:
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)
            return

        await interaction.response.send_message("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Join(bot))
