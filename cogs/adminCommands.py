import discord
from discord.ext import commands
from discord import app_commands


class amdinCommande(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="admin", description="Donne toutes les commandes du bot")
    async def amdinCommande_slash(self, interaction: discord.Interaction,):
        user = interaction.user  # Utilisateur exécutant la commande
        server_name = interaction.guild.name  # Nom du serveur

        embed = discord.Embed(title="Commande du bot",
                              description=f"Voici les commandes du bot ci-dessous",
                              color=0xff0000)
        embed.add_field(name="/mute_infinity", value="Mute le casque et micro de __**façon permanente**__ pour la personne choisie sans possibilité de retour en arrière", inline=False)
        embed.add_field(name="/deconnexion_infinity", value="Déconnecte l'utilisateur de __**façon permanente**__ pour la personne choisie sans possibilité de retour en arrière", inline=False)
        embed.add_field(name="/deafen", value="Mute le casque pour la personne choisie avec une possibilté de retour en arrière", inline=False)
        embed.add_field(name="/ban", value="Permet __**ban**__ un utilisateur du serveur", inline=False)
        embed.add_field(name="/kick", value="Permet __**kick**__ un utilisateur du serveur", inline=False)
        embed.add_field(name="/disconnect", value="Permet de  ___**déconnecter**___ un utilisateur choisi de son vocal", inline=False)
        embed.add_field(name="/membermove", value="Permet de ___**déplacer**___ un utilisateur choisi de son vocal", inline=False)
        embed.add_field(name="/clear", value="Permet de __**supprimer**__ les messages du salon écrit", inline=False)

        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

        print(f"Server : {server_name}")
        print(f"Commande help fait par : {user.name}#{user.discriminator} | {user.id} ")
        
        print("-------------------------------")

    @amdinCommande_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Le bot n'a pas les permissions pour pouvoir envoyer le message", ephemeral=True)


async def setup(bot):
    await bot.add_cog(amdinCommande(bot))
