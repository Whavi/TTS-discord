import discord
from discord.ext import commands
from discord import app_commands


class userInfo(commands.Cog):
    # Constructeur de la classe Join
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info_utilisateur", description="Donne les informations sur un Utilisateur")
    async def music_slash(self, interaction: discord.Interaction, membre: discord.Member):

        if membre is None:
            membre = interaction.user
        elif membre is not None:
            membre = membre

        membre_id = membre.id
        membre_name = membre.name
        membre_nameServer = membre.display_name
        membre_status = membre.status
        membre_info_create = membre.created_at.__format__("%A %d %B %Y")

        embed = discord.Embed(title="Information Utilisateur", color=0xff0000)
        embed.add_field(name="Pseudo :", value=membre_name, inline=False)
        embed.add_field(name="Pseudo Serveur :",
                        value=membre_nameServer, inline=False)
        embed.add_field(name="ID :", value=membre_id, inline=False)
        embed.add_field(name="Status :", value=membre_status, inline=False)
        embed.add_field(name="Crée depuis le ",
                        value=membre_info_create, inline=False)

        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(userInfo(bot))
