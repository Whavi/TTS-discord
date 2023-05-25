import asyncio
import discord
from discord.ext import commands
from discord import app_commands


class muteDefean(commands.Cog):
    # Constructeur de la classe muteDefean
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="deafen", description="Mute le casque de façon permanente pour la personne choisie")
    # Seulement les administrateurs peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def muteDefean_slash(self, interaction: discord.Interaction, membre: discord.Member, active: bool):
        users = interaction.user  # L'utilisateur qui a déclenché la commande
        server_name = interaction.guild.name  # Le nom du serveur
        voice_client_membre = membre.voice

        if not voice_client_membre:
            # L'utilisateur n'est pas connecté dans un salon vocal
            embed = discord.Embed(title="Mute Casque",
                                  description=f"{membre.display_name} n'est pas connecté dans un salon vocal.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        await membre.edit(deafen=active)  # Activer ou désactiver le mute du casque
        if active:
            action_text = "a été rendu sourd"
        else:
            action_text = "n'est plus rendu sourd"
        embed = discord.Embed(title="Mute Casque",
                              description=f"La personne {membre.mention} {action_text} dans le salon vocal.",
                              color=0xff0000)
        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

        print(f"Server : {server_name} ")
        print(f"ID user : {users.id}")
        print(
            f"La personne {membre.name} a été rendue sourde dans le salon vocal par {users.name}#{users.discriminator} | {users.display_name}")
        print("-------------------------------")

    @muteDefean_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Vous n'avez pas les permissions")


async def setup(bot):
    await bot.add_cog(muteDefean(bot))
