from sqlalchemy import Table, Column, String, Integer, DateTime, func
from config import meta, engine

Model_pets = Table(
    "pets",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("age", Integer),
    Column("owner", Integer),
    
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)

meta.create_all(engine)