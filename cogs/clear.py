import discord
from discord.ext import commands
from discord import app_commands


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="suprimme le nombre de message choisi")
    @app_commands.default_permissions(administrator=True)
    async def clear_slash(self, interaction: discord.Interaction, nombre: int):
        user = interaction.user  # l'utilisateur
        server_name = interaction.guild.name  # le nom du serveur
        channel_name = interaction.channel.name  # le salon vocal du serveur
        user = interaction.user  # Récupérer l'instance de l'utilisateur

        embed = discord.Embed(title="Clear",
                              description=f"Vous avez supprimé {nombre} message(s)",
                              color=0xff0000)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=nombre)
        print(f"Server : {server_name} ")
        print(f"Salon : {channel_name} ")
        print(f"ID : {user.id}")
        print(f"{user.name} a clear {nombre} message")
        print("-------------------------------")

    @clear_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions pour pouvoir supprimer les messages", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Clear(bot))
