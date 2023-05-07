import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    # Constructeur de la classe ping
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Affiche le ping du bot")
    # seuelement les administrateur peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def ping_slash(self, interaction: discord.Interaction):
        embed = discord.Embed(title=" Ping du bot",
                              description=f"le ping du bot est de {round(self.bot.latency * 1000)} ms",
                              color=0xff0000)
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @ping_slash.error
    async def say_error(selself, interaction: discord.Interaction, error):
        await interaction.response.send_message("Vous n'avez pas les permissions")


async def setup(bot):
    await bot.add_cog(Ping(bot))
