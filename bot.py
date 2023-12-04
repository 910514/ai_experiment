import re
# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
token = "token"
# intents是要求機器人的權限
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello, world!")

@bot.command()
async def update_api(ctx):
    # 執行 updata_weather_api.py 
    try:
        import subprocess
        subprocess.run(["python", "update_weather_api.py"])
        await ctx.send("Weather API updated successfully.")
    except Exception as e:
        await ctx.send(f"Error updating weather API: {e}")
@bot.command()
async def weather(ctx):
    try:
        import subprocess
        subprocess.run(["python", "weather.py"])
        # Open the image file in binary mode
        with open('pop12h.png', 'rb') as f:
            # Send the file as an attachment
            await ctx.send(file=discord.File(f, 'pop12h.png'))
        with open('average_temp.png', 'rb') as f:
            # Send the file as an attachment
            await ctx.send(file=discord.File(f, 'average_temp.png'))
        with open('maxAT.png', 'rb') as f:
            # Send the file as an attachment
            await ctx.send(file=discord.File(f, 'maxAT.png'))
        subprocess.run(["python", "api.py"])
        with open('output_api.txt', 'r', encoding='utf-8') as file:
            output_api_content = file.read()
        await ctx.send(output_api_content)
    except Exception as e:
        await ctx.send(f"Error when generating chart:{e}")

@bot.command()
async def llama2(ctx):
    try:
        #import subprocess
        #subprocess.run(["python", "api.py"])
        with open('output_api.txt', 'r', encoding='utf-8') as file:
            output_api_content = file.read()
        await ctx.send(output_api_content)
    except Exception as e:
        await ctx.send(f"Error when generating ai response:{e}")


bot.run(token)