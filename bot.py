import logging  # Import logging module for logging events
from aiogram import Bot, Dispatcher, executor  # Import necessary classes from aiogram
from config import BOT_TOKEN  # Import the bot token from the configuration file
from database import init_db  # Import the database initialization function
from handlers.notes import register_handlers  # Import the function to register command handlers

# Configure logging to output informational messages
logging.basicConfig(level=logging.INFO)

# Initialize the bot with the provided token
bot = Bot(token=BOT_TOKEN)

# Create a dispatcher to handle the bot's events
dp = Dispatcher(bot)

# Register the command handlers with the dispatcher
register_handlers(dp)

# Entry point of the script
if __name__ == '__main__':
    init_db()  # Initialize the database
    # Start polling for updates from Telegram, skipping updates that were missed while the bot was offline
    executor.start_polling(dp, skip_updates=True)
