import discord
from discord.ext import commands
from discord import app_commands


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban un utilisateur du serveur")
    @app_commands.default_permissions(administrator=True)
    async def ban_slash(self, interaction: discord.Interaction, membre: discord.Member, reason: str = None):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name

        if not reason:
            reason = "Aucune raison spécifiée"

        # Création de l'embed pour afficher le résultat du ban
        embed = discord.Embed(title="Ban",
                              description=f"L'utilisateur {membre.mention} a été banni du serveur.",
                              color=0xff0000)
        embed.add_field(name="Raison", value=reason, inline=False)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        # Envoi de l'embed en réponse à l'interaction
        await interaction.response.send_message(embed=embed, ephemeral=True)
        # Bannissement de l'utilisateur
        await membre.ban(reason=reason)

        # Affichage des informations du ban dans la console
        print(f"Server : {server_name}")
        print(f"Utilisateur banni : {membre.name} ({membre.id})")
        print(f"Banni par : {user.name} ({user.id})")
        print(f"Raison : {reason}")
        print("-------------------------------")

    @ban_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions pour pouvoir supprimer les messages", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Ban(bot))
