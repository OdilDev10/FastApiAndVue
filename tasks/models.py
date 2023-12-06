from sqlalchemy import Table, Column, Integer, String, DateTime, func
from db.db_config_sql import engine, meta

Model_tasks = Table(
    "tasks",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

meta.create_all(engine)
