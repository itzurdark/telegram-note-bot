from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
DATABASE_URL = 'sqlite:///./notes.db'

# Create a database engine
engine = create_engine(DATABASE_URL)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for declarative class definitions
Base = declarative_base()

# Define the Note model
class Note(Base):
    __tablename__ = 'notes'  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    user_id = Column(Integer, nullable=False)  # Column for the user ID
    text = Column(Text, nullable=False)  # Column for the note text
    bg_image_url = Column(String, nullable=True)  # Optional column for background image URL

# Define the User model
class User(Base):
    __tablename__ = 'users'  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    user_id = Column(Integer, unique=True, nullable=False)  # Unique column for the user ID
    telegraph_token = Column(String, nullable=True)  # Optional column for Telegraph token

def init_db():
    """
    Initialize the database by creating all tables.
    """
    Base.metadata.create_all(bind=engine)  # Create all tables in the database
