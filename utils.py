from database import SessionLocal, Note, User

# Initialize a database session
db = SessionLocal()

def get_note_by_id(db, user_id: int, note_id: int):
    """
    Retrieve a specific note by user ID and note ID.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.
    note_id (int): The ID of the note.

    Returns:
    Note: The note object if found, otherwise None.
    """
    return db.query(Note).filter(Note.user_id == user_id, Note.id == note_id).first()

def get_notes_by_user_id(db, user_id: int):
    """
    Retrieve all notes for a specific user.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.

    Returns:
    list: A list of note objects.
    """
    return db.query(Note).filter(Note.user_id == user_id).all()

def create_note(db, user_id: int, text: str):
    """
    Create a new note for a user.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.
    text (str): The text content of the note.

    Returns:
    Note: The newly created note object.
    """
    note = Note(user_id=user_id, text=text)  # Create a new Note object
    db.add(note)  # Add the note to the session
    db.commit()  # Commit the transaction
    db.refresh(note)  # Refresh the note instance to load the new ID
    return note

def update_note(db, user_id: int, note_id: int, new_text: str):
    """
    Update the text of an existing note.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.
    note_id (int): The ID of the note.
    new_text (str): The new text content for the note.

    Returns:
    bool: True if the note was updated, otherwise False.
    """
    note = get_note_by_id(db, user_id, note_id)  # Retrieve the note by ID
    if note:
        note.text = new_text  # Update the note text
        db.commit()  # Commit the transaction
        return True
    return False

def delete_note(db, user_id: int, note_id: int):
    """
    Delete a specific note by user ID and note ID.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.
    note_id (int): The ID of the note.

    Returns:
    bool: True if the note was deleted, otherwise False.
    """
    note = get_note_by_id(db, user_id, note_id)  # Retrieve the note by ID
    if note:
        db.delete(note)  # Delete the note from the session
        db.commit()  # Commit the transaction
        return True
    return False

def get_user(db, user_id: int):
    """
    Retrieve a user by their user ID.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.

    Returns:
    User: The user object if found, otherwise None.
    """
    return db.query(User).filter(User.user_id == user_id).first()

def create_user(db, user_id: int, telegraph_token: str):
    """
    Create a new user with a Telegraph token.
    
    Parameters:
    db (Session): The database session.
    user_id (int): The ID of the user.
    telegraph_token (str): The Telegraph token for the user.

    Returns:
    User: The newly created user object.
    """
    user = User(user_id=user_id, telegraph_token=telegraph_token)  # Create a new User object
    db.add(user)  # Add the user to the session
    db.commit()  # Commit the transaction
    db.refresh(user)  # Refresh the user instance to load the new ID
    return user
