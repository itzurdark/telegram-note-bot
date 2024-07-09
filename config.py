import os  # Import the os module for interacting with the operating system

# Retrieve the bot token from environment variables, with a default fallback value
BOT_TOKEN = os.getenv('BOT_TOKEN', 'TOKEN')
