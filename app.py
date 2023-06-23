
import asyncio
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

bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)
intents.guilds = True
intents.members = True


# Affiche un message dans la console quand le bot est prêt

@bot.event
async def on_ready():
    print(f'Le bot {bot.user.name} est prêt !')
    print(f"ID : {bot.user.id}")
    print("-------------------------------")
     
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if filename[:-3] not in ["view"]:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"le cog {filename} est bien charger !")

    try:
        synced = await bot.tree.sync()
        print("-------------------------------")
        print(f"syncro {len(synced)} commands")
        print("-------------------------------")
    except Exception as e:
        print(e)
    
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Tape sur Alexys'))
    

# Commande pour rejoindre le salon vocal de l'utilisateur

@bot.command(name='join')
async def join(ctx):
    await ctx.message.delete()
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


# Commande pour quitter le salon vocal de l'utilisateur


@bot.command(name='leave')
async def leave(ctx):
    await ctx.message.delete()
    server_name = ctx.guild.name
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client
    if voice_client:
        if voice_client.is_playing():
            voice_client.stop()
        await voice_client.disconnect()
        await print(f"Déconnecté du salon vocal {voice_channel.name} dans le serveur de {server_name}.")

    else:
        await ctx.send("Je ne suis pas connecté à un salon vocal.")

# Commande pour transcrire un message en audio


@bot.command()
async def tts(ctx, *args: str):
    await ctx.message.delete()
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

    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")


# Commande pour transcrire le dernier message en audio

@bot.command()
async def replay(ctx):
    await ctx.message.delete()
    user = ctx.message.author
    if user.voice is not None:
        try:
            vc = await user.voice.channel.connect()
        except:
            vc = ctx.voice_client
            source = FFmpegPCMAudio('audio.wav')
            vc.play(source)
    else:
        await ctx.send("Le bot n'est pas connecter dans votre salon")


@bot.command()
async def disconnect(ctx, member: discord.Member):
    # Vérifie si le membre spécifié est dans un canal vocal
    if member.voice and member.voice.channel:
        # Déconnecte le membre du canal vocal
        await member.voice.channel.move_to(None)
        await ctx.send(f"Le membre **__{member.display_name}__** a été déconnecté.")
    else:
        await ctx.send(f"Le membre {member.display_name} n'est pas connecté à un canal vocal.")


@bot.command()
async def clear(ctx, nombre: int):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.message.delete()
        await ctx.send("Vous n'avez pas les permissions pour supprimer les messages")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)
        return

    async for message in ctx.channel.history(limit=nombre):
        await message.delete()
        await asyncio.sleep(0.21)
    

# Lance le bot
bot.run(TOKEN)
