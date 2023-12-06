from fastapi import status, Response
from sqlalchemy import or_, select
from tasks.models import Model_tasks
from db.db_config_sql import database
from tasks.schemas import Schema_tasks, Schema_tasks_create_or_update


async def all_tasks(page: int = 1, limit: int = 10, search_term: str = ""):
    if search_term:
        query = (
            select(Model_tasks)
            .where(
                or_(
                    Model_tasks.c.name.ilike(f"%{search_term}%"),
                    Model_tasks.c.description.ilike(f"%{search_term}%"),
                )
            )
            .offset((page - 1) * limit)
            .limit(limit)
        )
    else:
        query = select(Model_tasks).offset((page - 1) * limit).limit(limit)

    return {
        "tasks": await database.fetch_all(query),
        "page": page,
        "limit": limit,
        "search_term": search_term,
    }


async def create_tasks(element: Schema_tasks_create_or_update):
    new_element = {"name": element.name, "description": element.description}
    operation = await database.execute(Model_tasks.insert().values(new_element))
    find = await database.fetch_one(
        Model_tasks.select().where(Model_tasks.c.id == operation)
    )
    return {"task": find, "message": "Task created successfully"}


async def find_one_tasks(id: str | int):
    return await database.fetch_one(Model_tasks.select().where(Model_tasks.c.id == id))


async def update_tasks(id: str | int, element: Schema_tasks_create_or_update):
    await database.fetch_one(
        Model_tasks.update()
        .values(name=element.name, description=element.description)
        .where(Model_tasks.c.id == id)
    )
    find = await database.fetch_one(Model_tasks.select().where(Model_tasks.c.id == id))
    return {"task": find, "message": "Task updated successfully"}


async def destroy_tasks(id: str | int):
    await database.fetch_one(Model_tasks.delete().where(Model_tasks.c.id == id))
    return {
        "status": status.HTTP_204_NO_CONTENT,
        "message": "Task deleted successfully",
    }
