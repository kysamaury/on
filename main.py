import os
import asyncio
from threading import Thread
from flask import Flask
from discord.ext import commands

# 1. Web server setup to satisfy Render's health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Online 24/7"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# 2. Discord self-bot setup
bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user}")

if __name__ == "__main__":
    # Run Flask in a background thread
    Thread(target=run_web).start()
    
    # Start the Discord bot using your token
    token = os.environ.get("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("Error: DISCORD_TOKEN variable not found.")
