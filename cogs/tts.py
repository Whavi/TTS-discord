import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
from gtts import gTTS


class tts(commands.Cog):
    # Constructeur de la classe tts
    def __init__(self, bot):
        self.bot = bot

    # Commande du /tts

    @app_commands.command(name="tts", description="Premet de faire le Text to speech au bot")
    async def tts_slash(self, interaction: discord.Interaction, message: str):
        user = interaction.user  # Récupérer l'instance de l'utilisateur
        # Récupérer l'instance du text de l'utilisateur
        if user.voice != None:
            try:
                # Essayer de se connecter dans le salon de l'utilisateur sans se deconnecter
                vc = await user.voice.channel.connect()
            except:
                # Sinon rejondre l'utilisateur dans un autre salon sans se deconnecter
                vc = user.guild.voice_client

            # text_to_speak = f"{user.author.name} dit : {text}" ( manière de savoir qui à écrit le message )
            sound = gTTS(text=message, lang="fr", slow=False)
            sound.save("audio.wav")
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
            embed = discord.Embed(title=" TTS request",
                                  description=f"Le message est bien envoyer",
                                  color=0xff0000)
            embed.set_author(name="TTSRomnisa",
                             icon_url="https://cdn.discordapp.com/attachments/858697367603249183/1103823004930158632/shay-jolie-clip.jpg")
            embed.set_footer(text="Bot fait par Whavi !")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @tts_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(tts(bot))
