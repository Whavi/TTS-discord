import discord
from discord.ext import commands
from discord import app_commands


class helpCommande(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Donne toutes les commandes du bot")
    async def helpCommande_slash(self, interaction: discord.Interaction,):
        user = interaction.user  # Utilisateur exécutant la commande
        server_name = interaction.guild.name  # Nom du serveur

        embed = discord.Embed(title="Commande du bot",
                              description=f"Voici les commandes du bot ci-dessous",
                              color=0xff0000)
        embed.add_field(name="/tts", value="Permet de faire la __**synthèse vocale de ce que vous écrivez en FRANCAIS**__ (Text-to-Speech) avec le bot ", inline=False)
        embed.add_field(name="/replay", value="Permet de ___**rejouer**___ le dernier son Text-to-Speech du bot", inline=False)
        embed.add_field(name="/join", value="Permet de ___**connecter**___ venir le bot dans votre salon", inline=False)
        embed.add_field(name="/leave", value="Permet de  ___**déconnecter**___ le bot du salon ", inline=False)
        embed.add_field(name="/ping", value="Permet de voir le ping du bot en ms ", inline=False)
        embed.add_field(name="/info_utilisateur", value="Permet de voir ___**les informations**___ de l'utilisateur choisi", inline=False)

        embed.set_author(name="TTSRomnisa",
                         icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
        embed.set_footer(text="Bot fait par Whavi !")
        await interaction.response.send_message(embed=embed, ephemeral=True)

        print(f"Server : {server_name}")
        print(f"Commande help fait par : {user.name}#{user.discriminator} | {user.id} ")
        
        print("-------------------------------")

    @helpCommande_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Le bot n'a pas les permissions pour pouvoir envoyer le message", ephemeral=True)


async def setup(bot):
    await bot.add_cog(helpCommande(bot))
