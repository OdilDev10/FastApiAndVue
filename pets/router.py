from fastapi import APIRouter, status
from .controller import all_pets, create_pets, find_one_pets, update_pets, destroy_pets
from .schemas import Schema_pets_create_or_update

router_pets = APIRouter()


@router_pets.get("/pets", tags=["pets".upper()])
async def get_pets(page: int = 1, limit: int = 10, search_term: str = ""):
    try:
        return await all_pets(page=page, limit=limit, search_term=search_term)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_pets.post("/pets", tags=["pets".upper()])
async def post_pets(elemet: Schema_pets_create_or_update):
    try:
        return await create_pets(elemet)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_pets.get("/pets/{id}", tags=["pets".upper()])
async def get_one_pets(id):
    try:
        return await find_one_pets(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_pets.put("/pets/{id}", tags=["pets".upper()])
async def post_pets(id, elemet: Schema_pets_create_or_update):
    try:
        return await update_pets(id, elemet)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_pets.delete("/pets/{id}", tags=["pets".upper()])
async def post_pets(id):
    try:
        return await destroy_pets(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }
