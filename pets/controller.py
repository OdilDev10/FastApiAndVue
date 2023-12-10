from sqlalchemy import select, or_
from .models import Model_pets
from config import connection
from fastapi import status


async def all_pets(
    page="",
    limit="",
    search_term="",
):
    try:
        if search_term:
            query = connection.execute(
                Model_pets.select()
                .where(
                    or_(
                        Model_pets.c.name.ilike(f"%{search_term}%"),
                    )
                )
                .offset((page - 1) * limit)
                .limit(limit)
            )
        else:
            query = connection.execute(
                Model_pets.select().offset((page - 1) * limit).limit(limit)
            )

        return {
            "user": query.fetchall(),
            "page": page,
            "limit": limit,
            "search_term": search_term,
            "status_code": status.HTTP_200_OK,
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def create_pets(element):
    try:
        query = connection.execute(
            Model_pets.insert().values(
                name=element.name, age=element.age, owner=element.owner
            )
        )

        return {
            "message": "create successfully",
            "status_code": status.HTTP_200_OK,
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def find_one_pets(id: str | int):
    try:
        query = connection.execute(
            Model_pets.select().where(Model_pets.c.id == id)
        ).fetchall()
        return query
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def update_pets(id: str | int, element):
    try:
        connection.execute(
            Model_pets.update()
            .values(name=element.name, age=element.age, owner=element.owner)
            .where(Model_pets.c.id == id)
        )
        return {
            "pets": connection.execute(
                Model_pets.select().where(Model_pets.c.id == id)
            ).fetchall(),
            "message": "updated pets",
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def destroy_pets(id: str | int):
    try:
        connection.execute(Model_pets.delete().where(Model_pets.c.id == id))

        return {
            "status_code": status.HTTP_204_NO_CONTENT,
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }
