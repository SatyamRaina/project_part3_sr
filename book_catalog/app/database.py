from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Fetch the database URL from environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Check if the DATABASE_URL is set, otherwise raise an error
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("No DATABASE_URL set for SQLAlchemy")

# Optional: Strip any accidental surrounding quotes
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.strip('"')

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configure session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for declarative models
Base = declarative_base()
