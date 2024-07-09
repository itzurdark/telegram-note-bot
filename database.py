from sqlalchemy import create_engine, Column, Integer, String, Text  # Import necessary SQLAlchemy components
from sqlalchemy.ext.declarative import declarative_base  # Import the base class for model definitions
from sqlalchemy.orm import sessionmaker  # Import sessionmaker to create database sessions

# Define the URL for the SQLite database
DATABASE_URL = 'sqlite:///./notes.db'

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models
Base = declarative_base()

# Define the Note model class
class Note(Base):
    __tablename__ = 'notes'  # Define the table name
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    user_id = Column(Integer, nullable=False)  # Column for the user ID, not nullable
    text = Column(Text, nullable=False)  # Column for the note text, not nullable
    bg_image_url = Column(String, nullable=True)  # Column for the background image URL, nullable

# Initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)
