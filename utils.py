from database import SessionLocal, Note  # Import the database session and Note model

# Create a new database session
db = SessionLocal()

# Function to get a note by its ID and user ID
def get_note_by_id(db, user_id: int, note_id: int):
    return db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).first()

# Function to get all notes by a user's ID
def get_notes_by_user_id(db, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()

# Function to create a new note
def create_note(db, user_id: int, text: str):
    note = Note(user_id=user_id, text=text)  # Create a new Note object
    db.add(note)  # Add the new note to the session
    db.commit()  # Commit the transaction to save the note in the database
    db.refresh(note)  # Refresh the note instance with the new data from the database
    return note  # Return the newly created note

# Function to update an existing note
def update_note(db, user_id: int, note_id: int, new_text: str):
    note = get_note_by_id(db, user_id, note_id)  # Retrieve the note by ID and user ID
    if note:
        note.text = new_text  # Update the note's text
        db.commit()  # Commit the transaction to save changes
        return True  # Return True if the note was found and updated
    return False  # Return False if the note was not found

# Function to delete an existing note
def delete_note(db, user_id: int, note_id: int):
    note = get_note_by_id(db, user_id, note_id)  # Retrieve the note by ID and user ID
    if note:
        db.delete(note)  # Delete the note from the session
        db.commit()  # Commit the transaction to remove the note from the database
        return True  # Return True if the note was found and deleted
    return False  # Return False if the note was not found
