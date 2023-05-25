import discord
from discord.ext import commands
from discord import app_commands


class MoveMember(commands.Cog):
    # Constructeur de la classe MoveMember
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="membermove", description="Change de salon une personne choisie, sinon c'est toi")
    # Seulement les administrateurs peuvent utiliser cette commande
    @app_commands.default_permissions(administrator=True)
    async def MoveMember_slash(self, interaction: discord.Interaction, channel: discord.channel.VoiceChannel, membre: discord.Member = None):
        # Récupération de l'utilisateur exécutant la commande
        user = interaction.user
        # Récupération du nom du serveur
        server_name = interaction.guild.name
        # Récupération du nom du salon vocal de l'utilisateur
        channel_name = user.voice.channel.name

        if not membre and (user.voice and user.voice.channel):
            # Déplacer l'utilisateur exécutant la commande vers le salon spécifié
            await user.move_to(channel)

            # Création de l'embed pour afficher le message de déplacement
            embed = discord.Embed(title="Changement de salon vocal réussi",
                                  description=f"L'utilisateur **__{user.name}__** a changé de salon vocal",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            # Affichage des informations de déplacement dans la console
            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a été déplacé dans {channel.name}")
            print("-------------------------------")

        if membre.voice and membre.voice.channel:
            # Déplacer le membre spécifié vers le salon spécifié
            await membre.move_to(channel)

            # Création de l'embed pour afficher le message de déplacement
            embed = discord.Embed(title="Changement de salon vocal réussi",
                                  description=f"L'utilisateur **__{membre.name}__** a changé de salon vocal",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            # Affichage des informations de déplacement dans la console
            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a déplacé {membre.name}#{membre.discriminator} | {membre.display_name} dans {channel.name}")
            print("-------------------------------")

        else:
            # Si le membre spécifié n'est pas dans un salon vocal
            embed = discord.Embed(title="Changement de salon vocal impossible",
                                  description=f"L'utilisateur {membre.name} n'a pas changé de salon vocal",
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
