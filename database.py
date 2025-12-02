from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost/escola"

# Criando o motor que faz a comunicação do DB com o fastAPI
engine = create_engine(DATABASE_URL)

# Estabelece a conexão com o DB e cria as sessões
SessionLocal = sessionmaker(bind=engine)

# Cria a classe base para gerir os modelos do DB
Base = declarative_base()
