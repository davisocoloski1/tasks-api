import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJCT_NAME: str = "Task API"
    DEBUG: bool = bool(os.getenv("DEBUG", False))

    # Databse connection (PostgreSQL - Sync with psycopg2)
    DB_USER: str = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    DB_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    DB_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    DB_NAME: str = os.getenv("POSTGRES_DB", "tasks_api")
    DATABASE_URL: str = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Auth (JWT)
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("ERROR: SECRET_KEY is missing in the .env file!")

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    if None in [DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]:
        raise ValueError("Variáveis de banco de dados ausentes no .env!")

# Instantiate the config
settings = Settings()