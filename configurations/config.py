import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    
    # Database
    DB_USER: str = "root"
    DB_PASSWORD: str = "root"
    DB_NAME: str = "fast_api"
    DB_HOST: str = "localhost"
    DB_PORT: str = "3306"
    DATABASE_URL: str = f"mysql+pymysql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}" % quote_plus(DB_PASSWORD)
    
    # JWT 
    JWT_SECRET: str = os.getenv('JWT_SECRET', '1782719222626171829271718929218')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('JWT_TOKEN_EXPIRE_MINUTES', 60)
    
def get_settings() -> Settings:
    return Settings()