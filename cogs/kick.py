import discord
from discord.ext import commands
from discord import app_commands


class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kick un utilisateur du serveur")
    @app_commands.default_permissions(administrator=True)
    async def kick_slash(self, interaction: discord.Interaction, membre: discord.Member, reason: str = None):
        user = interaction.user  # Utilisateur exécutant la commande
        server_name = interaction.guild.name  # Nom du serveur

        if not reason:
            reason = "Aucune raison spécifiée"

        # Création de l'embed pour afficher le message de kick
        embed = discord.Embed(title="Kick",
                              description=f"L'utilisateur {membre.mention} a été kick du serveur.",
                              color=0xff0000)
        embed.add_field(name="Raison", value=reason, inline=False)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")

        # Envoi de l'embed en réponse à l'interaction (message éphémère)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        # Exécution de la commande de kick sur le membre
        await membre.kick(reason=reason)

        # Affichage des informations de kick dans la console
        print(f"Server : {server_name}")
        print(f"Utilisateur kick : {membre.name} ({membre.id})")
        print(f"Kick par : {user.name} ({user.id})")
        print(f"Raison : {reason}")
        print("-------------------------------")

    @kick_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions pour pouvoir supprimer les messages", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Kick(bot))
