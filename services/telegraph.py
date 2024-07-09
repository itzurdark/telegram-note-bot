from telegraph import Telegraph
from utils import get_user, create_user, db

def create_telegraph_account(user_id: int, full_name: str):
    """
    Create a new Telegraph account for the user and save the access token in the database.
    
    Parameters:
    user_id (int): The unique ID of the user.
    full_name (str): The full name of the user.

    Returns:
    str: The access token for the Telegraph account.
    """
    telegraph = Telegraph()
    telegraph.create_account(short_name=full_name)  # Create a new Telegraph account with the user's full name
    telegraph_token = telegraph.get_access_token()  # Retrieve the access token for the Telegraph account
    create_user(db, user_id, telegraph_token)  # Save the user's data and Telegraph token in the database
    return telegraph_token

def get_telegraph_account(user_id: int, full_name: str):
    """
    Retrieve the Telegraph account for the user. If the user does not have a Telegraph account, create one.
    
    Parameters:
    user_id (int): The unique ID of the user.
    full_name (str): The full name of the user.

    Returns:
    Telegraph: The Telegraph account object.
    """
    user = get_user(db, user_id)  # Retrieve the user from the database
    if user and user.telegraph_token:
        # If the user exists and has a Telegraph token, initialize the Telegraph account with the token
        telegraph = Telegraph(user.telegraph_token)
    else:
        # If the user does not exist or does not have a Telegraph token, create a new Telegraph account
        telegraph_token = create_telegraph_account(user_id, full_name)
        telegraph = Telegraph(telegraph_token)
    return telegraph

def upload_to_telegraph(telegraph: Telegraph, note, full_name: str):
    """
    Upload the note to Telegraph and return the URL of the created page.
    
    Parameters:
    telegraph (Telegraph): The Telegraph account object.
    note: The note object containing the text and optional background image URL.
    full_name (str): The full name of the user.

    Returns:
    str: The URL of the created Telegraph page.
    """
    html_content = note.text  # Get the note text
    if note.bg_image_url:
        # If there is a background image URL, format it with the note text as HTML content
        html_content = f'<img src="{note.bg_image_url}" /><br>{note.text}'

    # Create a new page on Telegraph with the note's content
    response = telegraph.create_page(
        title=f'Note {note.id}',  # Use the note ID as the title
        author_name=full_name,  # Set the author name
        html_content=html_content  # Set the HTML content
    )
    return f"https://telegra.ph/{response['path']}"  # Return the URL of the created page
