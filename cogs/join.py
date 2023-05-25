import discord
from discord import app_commands
from discord.ext import commands


class Join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join", description="Rejoint le salon auquel tu es connecté")
    async def join_slash(self, interaction: discord.Interaction):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du salon vocal de l'utilisateur
        channel = interaction.user.voice.channel
        # Récupération du voice client du serveur
        voice_client = interaction.guild.voice_client

        if voice_client is None:
            # Si aucun voice client n'est présent, le bot se connecte au salon vocal de l'utilisateur
            await channel.connect()
        else:
            # Sinon, le bot se déplace directement vers le salon vocal de l'utilisateur
            await voice_client.move_to(channel)

        # Création de l'embed pour indiquer que le bot est connecté au salon vocal
        embed = discord.Embed(title="Connected",
                              description=f"Connecté au salon vocal {channel.name}",
                              color=0xff0000)
        embed.set_author(name=f"{user.name}",
                         icon_url=user.avatar)
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

        # Affichage des informations dans la console
        print(f"Server : {server_name}")
        print(f"Salon : {channel}")
        print(f"ID : {user.id}")
        print(f"{user.name} a fait rejoindre le bot")
        print("-------------------------------")

    @join_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'êtes pas connecté dans un salon vocal.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Join(bot))
