from flask import Flask
from . import config as cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

SQLALCHEMY_DB_URI = f"postgresql+psycopg2://{cfg.db['user']}:" \
    f"{cfg.db['password']}@{cfg.db['host']}/{cfg.db['dbase']}"

engine = create_engine(SQLALCHEMY_DB_URI, echo=False)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = DBSession()
db_base = declarative_base()


from .controllers import *
from .models import people
from .controllers.helpers import filters

db_base.metadata.create_all(engine)
