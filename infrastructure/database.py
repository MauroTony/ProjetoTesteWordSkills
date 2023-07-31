from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy usa uma URL de banco de dados para se conectar com o MySQL.
# Substitua os seguintes valores de acordo com a configuração do seu banco de dados.
DATABASE_URL = "mysql+pymysql://root:voyage2246@172.16.238.10:3306/projeto"

engine = create_engine(DATABASE_URL)

# Use `scoped_session` para garantir que a sessão seja encerrada após cada solicitação.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
