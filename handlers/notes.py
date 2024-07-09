from aiogram import types, Dispatcher  # Import necessary modules from aiogram
from database import SessionLocal  # Import the database session
from utils import get_note_by_id, create_note, update_note, delete_note, get_notes_by_user_id  # Import utility functions

# Initialize a session with the database
db = SessionLocal()

# Handler for the /start command
async def start_command(message: types.Message):
    await message.answer(
        "Welcome! Use /new to create a new note, /list to view all notes, /note to view a specific note, /edit to edit a note, and /delete to delete a note."
    )

# Handler for the /new command to create a new note
async def new_note_command(message: types.Message):
    note_text = message.get_args()
    if note_text:
        note = create_note(db, message.from_user.id, note_text)  # Create a new note
        await message.answer(f"Note created with ID: {note.id}")
    else:
        await message.answer("Please provide text for the new note.")  # Prompt user for note text if not provided

# Handler for the /list command to list all notes
async def list_notes_command(message: types.Message):
    notes = get_notes_by_user_id(db, message.from_user.id)  # Retrieve notes for the user
    if notes:
        response = "Your notes:\n"
        for note in notes:
            response += f"{note.id}: {note.text}\n"  # Format the response with note IDs and texts
        await message.answer(response)
    else:
        await message.answer("You have no notes.")  # Inform the user if there are no notes

# Handler for the /note command to view a specific note
async def view_note_command(message: types.Message):
    args = message.get_args()
    if not args.isdigit():
        await message.answer("Please provide a valid note ID.")  # Prompt user for a valid note ID
        return
    
    note_id = int(args)
    note = get_note_by_id(db, message.from_user.id, note_id)  # Retrieve the note by ID
    if note:
        await message.answer(note.text)  # Display the note text
    else:
        await message.answer("Note not found.")  # Inform the user if the note is not found

# Handler for the /delete command to delete a note
async def delete_note_command(message: types.Message):
    args = message.get_args()
    if not args.isdigit():
        await message.answer("Please provide a valid note ID.")  # Prompt user for a valid note ID
        return
    
    note_id = int(args)
    note = get_note_by_id(db, message.from_user.id, note_id)  # Retrieve the note by ID
    if note:
        if delete_note(db, message.from_user.id, note_id):  # Delete the note
            await message.answer("Note deleted.")
        else:
            await message.answer("An error occurred while deleting the note.")  # Handle deletion error
    else:
        await message.answer("Note not found. Please check the ID and try again.")  # Inform the user if the note is not found

# Handler for the /edit command to edit a note
async def edit_note_command(message: types.Message):
    args = message.get_args().split(maxsplit=1)
    if len(args) < 2 or not args[0].isdigit():
        await message.answer("Please provide the note ID and new text.")  # Prompt user for note ID and new text
        return

    note_id, new_text = int(args[0]), args[1]
    if update_note(db, message.from_user.id, note_id, new_text):  # Update the note
        await message.answer("Note updated.")
    else:
        await message.answer("Note not found.")  # Inform the user if the note is not found

# Handler for the /generate command to add an image URL to a note
async def generate_image_command(message: types.Message):
    args = message.get_args().split(maxsplit=1)
    if len(args) < 2 or not args[0].isdigit():
        await message.answer("Please provide the note ID and background image URL.")  # Prompt user for note ID and image URL
        return

    note_id, bg_image_url = int(args[0]), args[1]
    note = get_note_by_id(db, message.from_user.id, note_id)  # Retrieve the note by ID
    if note:
        note.bg_image_url = bg_image_url  # Add the image URL to the note
        db.commit()  # Commit the changes to the database
        await message.answer("Image URL saved.")
    else:
        await message.answer("Note not found.")  # Inform the user if the note is not found

# Function to register command handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(new_note_command, commands="new")
    dp.register_message_handler(list_notes_command, commands="list")
    dp.register_message_handler(view_note_command, commands="note")
    dp.register_message_handler(delete_note_command, commands="delete")
    dp.register_message_handler(edit_note_command, commands="edit")
    dp.register_message_handler(generate_image_command, commands="generate")
