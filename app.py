import asyncio
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from gtts import gTTS
import os
from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env

load_dotenv()

# Récupère le token d'authentification du bot
TOKEN = os.getenv('DISCORD_TOKEN')

# Crée le bot avec le préfixe "!"
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Affiche un message dans la console quand le bot est prêt


@bot.event
async def on_ready():
    print(f'Le bot {bot.user} est prêt !')

# Déconnecte le bot lorsqu'il n'y a plus personne dans le salon un certain temps


@bot.event
async def on_voice_state_update():
    if bot.voice_clients and bot.voice_clients[0].channel:
        channel = bot.voice_clients[0].channel
        if not channel.members:  # Aucun utilisateur dans le canal vocal
            await bot.voice_clients[0].disconnect()


# Commande pour rejoindre le salon vocal de l'utilisateur


@bot.command(name='join')
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Tu n'es pas connecté à un salon vocal.")
        return

    server_name = ctx.guild.name
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
    print(
        f"Connecté au salon vocal {voice_channel.name} dans le serveur de {server_name} !")
    await ctx.message.delete()

# Commande pour quitter le salon vocal de l'utilisateur


@bot.command(name='leave')
async def leave(ctx):
    server_name = ctx.guild.name
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client
    if voice_client:
        if voice_client.is_playing():
            voice_client.stop()
        await voice_client.disconnect()
        await print(f"Déconnecté du salon vocal {voice_channel.name} dans le serveur de {server_name}.")
        await ctx.message.delete()
    else:
        await ctx.send("Je ne suis pas connecté à un salon vocal.")

# Commande pour transcrire un message en audio


@bot.command()
async def tts(ctx, *args: str):
    text = " ".join(args)
    user = ctx.message.author
    if user.voice != None:
        try:
            vc = await user.voice.channel.connect()
        except:
            vc = ctx.voice_client

        # text_to_speak = f"{ctx.author.name} dit : {text}"
        sound = gTTS(text=text, lang="fr", slow=False)
        sound.save("audio.wav")
        source = FFmpegPCMAudio('audio.wav')
        vc.play(source)
        await ctx.message.delete()

    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")


# Commande pour transcrire le dernier message en audio

@bot.command()
async def replay(ctx):
    user = ctx.message.author
    if user.voice is not None:
        try:
            vc = await user.voice.channel.connect()
        except:
            vc = ctx.voice_client
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
        await ctx.message.delete()
    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")

# Lance le bot
bot.run(TOKEN)
