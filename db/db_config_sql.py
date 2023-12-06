from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./test.db"
meta = MetaData()
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
connection = engine
