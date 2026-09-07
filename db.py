from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker,declarative_base

# connect the mysql Server URL 
Server_url = "mysql+pymysql://root:root@localhost:3306"
cont=create_engine(Server_url)

# creat new DB if it is not exist
with cont.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS CV_cheacker_Fast_API"))  ## it is not a simple sting it is SQL Command 

# connect to the database
database_url = "mysql+pymysql://root:root@localhost:3306/CV_cheacker_Fast_API"
engine = create_engine(
    database_url,
    pool_pre_ping=True
    )

# local_session = sessionmaker(bind=engine)
Base = declarative_base()
# Import models AFTER Base is defined
from models import User,Report

# ✅ Create tables
Base.metadata.create_all(bind=engine)


# Session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


