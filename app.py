import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio
from gtts import gTTS
from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env

load_dotenv()

# Récupère le token d'authentification du bot
TOKEN = os.getenv('DISCORD_TOKEN')

# Crée le bot avec le préfixe "!"
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
intents.guilds = True
intents.members = True

# Affiche un message dans la console quand le bot est prêt


@bot.event
async def on_ready():
    print(f'Le bot {bot.user.name} est prêt !')
    print(f"ID : {bot.user.id}")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if filename[:-3] not in ["view"]:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"le cog {filename} est bien charger !")

    try:
        synced = await bot.tree.sync()
        print(f"syncro {len(synced)} commands")
    except Exception as e:
        print(e)

# Commande pour transcrire un message en audio


@bot.command()
async def tts(ctx, *args: str):
    text = " ".join(args)
    user = ctx.message.author
    server_name = ctx.guild.name
    channel_name = ctx.author.voice.channel.name
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
        print(f"Server : {server_name} ")
        print(f"Salon : {channel_name} ")
        print(f"ID : {user.id}")
        print(f"{user.name} a fait un replay de l'audio 'audio.wav' ")
        await ctx.message.delete()

    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")


# Commande pour transcrire le dernier message en audio

@bot.command()
async def replay(ctx):
    user = ctx.message.author
    server_name = ctx.guild.name
    channel_name = ctx.author.voice.channel.name

    if user.voice is not None:
        try:
            vc = await user.voice.channel.connect()
        except:
            vc = ctx.voice_client
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
            print(f"Server : {server_name} ")
            print(f"Salon : {channel_name} ")
            print(f"ID : {user.id}")
            print(f"{user.name} a fait un replay de l'audio 'audio.wav'")
        await ctx.message.delete()
    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")

# Lance le bot
bot.run(TOKEN)
