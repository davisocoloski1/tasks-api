from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Configura a URL do banco de dados
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Cria a engine de conexão com o PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configura a fábrica de sessões (usada nos endpoints da FastAPI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base que todos os modelos vão herdar
Base = declarative_base()