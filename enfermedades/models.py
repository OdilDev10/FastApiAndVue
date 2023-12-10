from sqlalchemy import Table, Column, String, Integer, DateTime, func
from config import meta, engine

Model_enfermedades = Table(
    "enfermedades",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),    
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)


meta.create_all(engine)