from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# import cloudinary

# cloudinary.config(
#     cloud_name= "df3xeo8qv",
#     api_key= "176527258737513",
#     api_secret ="-OC7IdktnaKk9DySFUkVH8QOL48"
# )

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()