from sqlalchemy import select, or_
from .models import Model_enfermedades
from config import connection
from fastapi import status


async def all_enfermedades(
    page="",
    limit="",
    search_term="",
):
    try:
        if search_term:
            query = connection.execute(
                Model_enfermedades.select()
                .where(
                    or_(
                        Model_enfermedades.c.email.ilike(f"%{search_term}%"),
                    )
                )
                .offset((page - 1) * limit)
                .limit(limit)
            )
        else:
            query = connection.execute(
                Model_enfermedades.select().offset((page - 1) * limit).limit(limit)
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


async def create_enfermedades(element):
    try:
        query = connection.execute(
            Model_enfermedades.insert().values(
                email=element.email,
                password=element.password,
                age=element.age,
                color=element.color,
            )
        )
        print(query, "query")

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


async def find_one_enfermedades(id: str | int):
    print(id, "--------------")
    try:
        query = connection.execute(
            Model_enfermedades.select().where(Model_enfermedades.c.id == id)
        ).fetchall()
        return query
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def update_enfermedades(id: str | int, element):
    try:
        connection.execute(
            Model_enfermedades.update()
            .values(email=element.email, password=element.password)
            .where(Model_enfermedades.c.id == id)
        )
        return {
            "enfermedades": connection.execute(
                Model_enfermedades.select().where(Model_enfermedades.c.id == id)
            ).fetchall(),
            "message": "updated enfermedades",
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


async def destroy_enfermedades(id: str | int):
    try:
        connection.execute(
            Model_enfermedades.delete().where(Model_enfermedades.c.id == id)
        )

        return {
            "status_code": status.HTTP_204_NO_CONTENT,
        }
    except Exception as error:
        print("-----Error controller: ", error)
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }
