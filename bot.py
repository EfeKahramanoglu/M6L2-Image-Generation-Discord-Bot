from logic import *

import discord
from discord.ext import commands


api = Imgapi()

intents = discord.Intents()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot başlatıldı!: {bot.user.name}")

@bot.command()
async def generate_image(ctx, *, prompt=""):
    if not prompt:
        await ctx.send("Lütfen bir prompt girin.")
        return

    try:

        image_path = api.download_image(prompt)
        await ctx.send(file=discord.File(image_path))

    except Exception as e:
        print(f"Resim indirilirken bir hata oluştu: {e}")
        await ctx.send("Resim indirilirken bir hata oluştu.")



if __name__ == "__main__":
    bot.run(TOKEN)

    