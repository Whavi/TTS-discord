import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
from gtts import gTTS

class tts(commands.Cog):
    # Constructeur de la classe tts
    def __init__(self, bot):
        self.bot = bot

    # Commande /tts
    @app_commands.command(name="tts", description="Permet de faire la synthèse vocale (Text-to-Speech) avec le bot")
    async def tts_slash(self, interaction: discord.Interaction, message: str):
        server_name = interaction.guild.name  # Nom du serveur
        channel_name = interaction.user.voice.channel.name  # Nom du salon vocal de l'utilisateur
        user = interaction.user  # Obtenir l'instance de l'utilisateur

        if user.voice is not None:
            try:
                # Essayer de se connecter dans le salon vocal de l'utilisateur sans se déconnecter
                vc = await user.voice.channel.connect()
            except:
                # Sinon rejoindre l'utilisateur dans un autre salon sans se déconnecter
                vc = user.guild.voice_client

            # Générer le fichier audio à partir du texte fourni
            sound = gTTS(text=message, lang="fr", slow=False)
            sound.save("audio.wav")

            # Charger le fichier audio et le jouer dans le salon vocal
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)

            embed = discord.Embed(title="TTS request",
                                  description="Le message a été envoyé avec succès.",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a effectué une synthèse vocale de 'audio.wav'")
            print(f"le message : {message}")
            print("-------------------------------")

    @tts_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        if not interaction.response.is_done():
            await interaction.response.send_message("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(tts(bot))
