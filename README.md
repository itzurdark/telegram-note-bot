# Telegram Note Bot

This bot allows you to create, view, edit, delete notes, and upload them to Telegraph.

## Setup

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Set your Telegram bot token in `config.py`.
4. Run the bot:
    ```sh
    python bot.py
    ```

## Commands

- `/start` - Welcome message.
- `/new [text]` - Create a new note.
- `/list` - List all notes.
- `/note [id]` - View a note by ID.
- `/edit [id] [new text]` - Edit a note by ID.
- `/delete [id]` - Delete a note by ID.
- `/generate [id] [background image URL]` - Generate an image with the note text.