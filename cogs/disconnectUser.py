import discord
from discord.ext import commands
from discord import app_commands


class DisconnectUser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="disconnect", description="Déconnecte un utilisateur choisi")
    @app_commands.default_permissions(administrator=True)
    async def disconnectUser_slash(self, interaction: discord.Interaction, membre: discord.Member):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du nom du salon vocal de l'utilisateur
        channel_name = membre.voice.channel.name
        
        if membre.voice and membre.voice.channel:
            # Déplacement de l'utilisateur vers aucun salon vocal (déconnexion)
            await membre.move_to(None)

            embed = discord.Embed(title="Déconnexion réussie",
                                  description=f"L'utilisateur **{membre.name}** a été déconnecté.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            # Affichage des informations de déconnexion dans la console
            print(f"Server : {server_name}")
            print(f"Salon : {channel_name}")
            print(f"ID : {user.id}")
            print(f"{user.name} a déconnecté {membre.name}#{membre.discriminator} | {membre.display_name}")
            print("-------------------------------")

        else:
            embed = discord.Embed(title="Déconnexion impossible",
                                  description=f"L'utilisateur {membre.name} n'est pas connecté à un salon vocal.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/11038230²04930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @disconnectUser_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions pour effectuer cette action.")

async def setup(bot):
    await bot.add_cog(DisconnectUser(bot))
