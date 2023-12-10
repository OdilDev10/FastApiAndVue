from fastapi import FastAPI

# ROUTER

from enfermedades.router import router_enfermedades
from pets.router import router_pets



app = FastAPI(
    title="Mi API",
    description="Una API de ejemplo con FastAPI",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redocumentation",
    openapi_url="/myapi/openapi.json",
    debug=True,
)


app.include_router(prefix="/api", router=router_enfermedades)
app.include_router(prefix="/api", router=router_pets)




@app.get("/")
def read_root():
    return {"message": "Welcome app run on port 8000"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
