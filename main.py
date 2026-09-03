import os
import asyncio
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands

app = Flask(__name__)

@app.route('/')
def home():
    return "Online 24/7"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Initialize bot
bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user}")
    
    # Change status to Online (or discord.Status.dnd for Do Not Disturb)
    # and re-apply your custom status message
    await bot.change_presence(
        status=discord.Status.online, 
        activity=discord.CustomActivity(name="asleep 💀 ")
    )

if __name__ == "__main__":
    Thread(target=run_web).start()
    
    token = os.environ.get("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("Error: DISCORD_TOKEN variable not found.")
