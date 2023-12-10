from fastapi import APIRouter, status
from .controller import all_enfermedades, create_enfermedades, find_one_enfermedades, update_enfermedades, destroy_enfermedades
from .schemas import Schema_enfermedades_create_or_update

router_enfermedades = APIRouter()


@router_enfermedades.get("/enfermedades", tags=["enfermedades".upper()])
async def get_enfermedades(page: int = 1, limit: int = 10, search_term: str = ""):
    try:
        return await all_enfermedades(page=page, limit=limit, search_term=search_term)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_enfermedades.post("/enfermedades", tags=["enfermedades".upper()])
async def post_enfermedades(elemet: Schema_enfermedades_create_or_update):
    try:
        return await create_enfermedades(elemet)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_enfermedades.get("/enfermedades/{id}", tags=["enfermedades".upper()])
async def get_one_enfermedades(id):
    try:
        return await find_one_enfermedades(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_enfermedades.put("/enfermedades/{id}", tags=["enfermedades".upper()])
async def post_enfermedades(id, elemet: Schema_enfermedades_create_or_update):
    try:
        return await update_enfermedades(id, elemet)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }


@router_enfermedades.delete("/enfermedades/{id}", tags=["enfermedades".upper()])
async def post_enfermedades(id):
    try:
        return await destroy_enfermedades(id)
    except Exception as error:
        return {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "detail": str(error),
        }
