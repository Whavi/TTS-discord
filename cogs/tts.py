import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio
from gtts import gTTS


class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tts", description="Premet de faire le Text to speech au bot")
    async def tts_slash(self, interaction: discord.Interaction, *, message: str):
        args = message
        user = args.user.author
        text = " ".join(args)
        if user.voice != None:
            try:
                vc = await user.voice.channel.connect()
            except:
                vc = user.guild.voice_client

            # text_to_speak = f"{user.author.name} dit : {text}"
            sound = gTTS(text=text, lang="fr", slow=False)
            sound.save("audio.wav")
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
        else:
            await interaction.response.send_message("Le bot n'est pas connecter dans votre salon")

    @tts_slash.error
    async def say_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(tts(bot))
