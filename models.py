from sqlalchemy import Column, Integer, String, Text  # Import necessary SQLAlchemy components for column types
from sqlalchemy.ext.declarative import declarative_base  # Import the base class for model definitions

# Create a base class for the models
Base = declarative_base()

# Define the Note model class
class Note(Base):
    __tablename__ = 'notes'  # Define the table name
    id = Column(Integer, primary_key=True, index=True)  # Primary key column with indexing
    user_id = Column(Integer, nullable=False)  # Column for the user ID, not nullable
    text = Column(Text, nullable=False)  # Column for the note text, not nullable
    bg_image_url = Column(String, nullable=True)  # Column for the background image URL, nullable
