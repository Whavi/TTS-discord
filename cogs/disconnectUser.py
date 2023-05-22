import discord
from discord.ext import commands
from discord import app_commands


class disconnectUser(commands.Cog):
    # Constructeur de la classe ping
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="disconnect", description="Affiche le ping du bot")
    # seulement les administrateur peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def disconnectUser_slash(self, interaction: discord.Interaction, membre: discord.Member):

        user = interaction.user
        server_name = interaction.guild.name
        channel_name = user.voice.channel.name

        if membre.voice and membre.voice.channel:
            await membre.move_to(None)

            embed = discord.Embed(title="Deconnexion réussi ",
                                  description=f"L'utilisateur **__{membre.name}__** à été deconnecté",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(
                f"{user.name} a fait un déconnecté {membre.name}#{membre.discriminator} | {membre.display_name}")
            print("-------------------------------")

        else:
            embed = discord.Embed(title="Deconnexion Impossible ",
                                  description=f"L'utilisateur {membre.name} n'est pas connecté",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @disconnectUser_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions")


async def setup(bot):
    await bot.add_cog(disconnectUser(bot))
