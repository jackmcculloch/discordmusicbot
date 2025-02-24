import discord
from discord.ext import commands
import subprocess
import os
import asyncio

# Replace with your bot token from Discord Developer Portal
TOKEN = "MTM0MzY3MjM0MjMyNDMxODI1OQ.G5_1_-.ICA6h0l0YxoupQZqr-uyUzgZwxXcXU6nAwYyPk"

# Set up the bot with a command prefix, e.g., "!"
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="play", help="Downloads audio from a URL and plays it in your voice channel")
async def play(ctx, url: str):
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send("You must be in a voice channel to use this command.")
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        voice_client = await voice_channel.connect()
    else:
        voice_client = ctx.voice_client
        if voice_client.channel != voice_channel:
            await voice_client.move_to(voice_channel)

    temp_filename = "song.mp3"
    await ctx.send("Pooping my stinky pants...")

    command = [
        "yt-dlp", "-x", "--audio-format", "mp3",
        "-o", temp_filename,
        url
    ]

    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        await ctx.send("Failed to download audio. Please check the URL and try again.")
        print("yt-dlp error:", process.stderr)
        return

    await ctx.send("Playing audio...")
    audio_source = discord.FFmpegPCMAudio(temp_filename)
    voice_client.play(audio_source)

    while voice_client.is_playing():
        await asyncio.sleep(1)

    await voice_client.disconnect()

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    await ctx.send("Finished pooping and threw out my stinky poopy undies")

@bot.command(name="stop", help="Stops playback and disconnects the bot")
async def stop(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send("Fine I'll'just go hang with Joe and Clevland")
    else:
        await ctx.send("I am not connected to any voice channel.")

if __name__ == "__main__":
    bot.run(TOKEN)
