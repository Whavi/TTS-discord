import discord
from discord.ext import commands
from discord import app_commands


class MoveMember(commands.Cog):
    # Constructeur de la classe ping
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="membermove", description="Affiche le ping du bot")
    # seulement les administrateur peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def MoveMember_slash(self, interaction: discord.Interaction, membre: discord.Member, channel: discord.channel.VoiceChannel):

        user = interaction.user
        server_name = interaction.guild.name
        channel_name = user.voice.channel.name

        if membre.voice and membre.voice.channel:
            await membre.move_to(channel)

            embed = discord.Embed(title="Changement de salon vocal réussi ",
                                  description=f"L'utilisateur **__{membre.name}__** à changer de vocal",
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
            embed = discord.Embed(title="Changement de salon vocal Impossible ",
                                  description=f"L'utilisateur {membre.name} n'a pas changer de vocal",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @MoveMember_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions")


async def setup(bot):
    await bot.add_cog(MoveMember(bot))
