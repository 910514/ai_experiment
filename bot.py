import re
import discord
from discord.ext import commands, tasks
import datetime

token = "dc_token"
# intents是要求機器人的權限
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
target_channel_id = "1005070106746966117"

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    daily_task.start()

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
        try:
            subprocess.run(["python", "update_weather_api.py"])
            await ctx.send("Weather API updated successfully.")
        except Exception as e:
            await ctx.send(f"Error updating weather API: {e}")
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
        subprocess.run(["python", "chatanywhere.py"])
        with open('output_api.txt', 'r', encoding='utf-8') as file:
            output_api_content = file.read()
            result = re.sub(r'^.*?\'role\': \'assistant\', \'content\': \'(.*?)\'}.*?$', r'\1', output_api_content, flags=re.DOTALL)
            result = result.rstrip("']")
            final_result = result.replace(r'\n', '\n')
        await ctx.send(f'```plaintext\n{final_result}\n```')
    except Exception as e:
        await ctx.send(f"Error when generating response:{e}")

@bot.command()
async def llama2(ctx):
    try:
        with open('output_api.txt', 'r', encoding='utf-8') as file:
            output_api_content = file.read()
            final_result = re.sub(r'^.*?\'.*?\'.*?\'', '', output_api_content)
            final_result = final_result.rstrip("']")
            final_result = final_result.replace(r'\n', '\n')
            await ctx.send(f'```plaintext\n{final_result}\n```')
    except Exception as e:
        await ctx.send(f"Error when generating ai response:{e}")

@bot.command()
async def chatgpt(ctx):
    try:
        with open('output_api.txt', 'r', encoding='utf-8') as file:
            output_api_content = file.read()
            result = re.sub(r'^.*?\'role\': \'assistant\', \'content\': \'(.*?)\'}.*?$', r'\1', output_api_content, flags=re.DOTALL)
            result = result.rstrip("']")
            final_result = result.replace(r'\n', '\n')
        await ctx.send(f'```plaintext\n{final_result}\n```')
    except Exception as e:
        await ctx.send(f"Error when generating ai response:{e}")

@tasks.loop(seconds=30)
async def daily_task():
    now = datetime.datetime.now().time()
    target_time = datetime.time(7, 00)  # Set the target time (7:00 AM)

    if now.hour == target_time.hour and now.minute == target_time.minute:
        try:
            import subprocess
            try:
                subprocess.run(["python", "update_weather_api.py"])
                channel = bot.get_channel(int(target_channel_id))
                await channel.send("Weather API updated successfully.")
            except Exception as e:
                channel = bot.get_channel(int(target_channel_id))
                await channel.send(f"Error updating weather API: {e}")
                
            subprocess.run(["python", "weather.py"])
            
            channel = bot.get_channel(int(target_channel_id))
            
            with open('pop12h.png', 'rb') as f:
                await channel.send(file=discord.File(f, 'pop12h.png'))
            with open('average_temp.png', 'rb') as f:
                await channel.send(file=discord.File(f, 'average_temp.png'))
            with open('maxAT.png', 'rb') as f:
                await channel.send(file=discord.File(f, 'maxAT.png'))
                
            subprocess.run(["python", "chatanywhere.py"])
            
            with open('output_api.txt', 'r', encoding='utf-8') as file:
                output_api_content = file.read()
                result = re.sub(r'^.*?\'role\': \'assistant\', \'content\': \'(.*?)\'}.*?$', r'\1', output_api_content, flags=re.DOTALL)
                result = result.rstrip("']")
                final_result = result.replace(r'\n', '\n')
                
            await channel.send(f'```plaintext\n{final_result}\n```')
            
        except Exception as e:
            channel = bot.get_channel(int(target_channel_id))
            await channel.send(f"Error when generating response: {e}")




bot.run(token)