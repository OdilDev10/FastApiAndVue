from fastapi import APIRouter, HTTPException
from fastapi import status, Response
from tasks.controller import (
    all_tasks,
    create_tasks,
    find_one_tasks,
    update_tasks,
    destroy_tasks,
)
from tasks.schemas import Schema_tasks, Schema_tasks_create_or_update

router_tasks = APIRouter()


@router_tasks.get("/tasks", tags=["tasks".upper()])
async def get_tasks(page: int = 1, limit: int = 10, search_term: str = ""):
    try:
        return await all_tasks(page=page, limit=limit, search_term=search_term)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )


@router_tasks.post(
    "/tasks", response_model=Schema_tasks_create_or_update, tags=["tasks".upper()]
)
async def post_tasks(carro: Schema_tasks_create_or_update):
    try:
        return await create_tasks(carro)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


@router_tasks.get("/tasks/{id}", response_model=Schema_tasks, tags=["tasks".upper()])
async def get_one_tasks(id: str | int):
    try:
        return await find_one_tasks(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


@router_tasks.put(
    "/tasks/{id}", response_model=Schema_tasks_create_or_update, tags=["tasks".upper()]
)
async def put_tasks(id: str | int, carro: Schema_tasks_create_or_update):
    try:
        return await update_tasks(id, carro)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }


@router_tasks.delete("/tasks/{id}", tags=["tasks".upper()])
async def delete_tasks(id: str | int):
    try:
        return await destroy_tasks(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(error),
        }
