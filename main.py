from fastapi import FastAPI
from tasks.router import router_tasks
from config import connection

app = FastAPI(
    title="Mi API",
    description="Una API de ejemplo con FastAPI",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redocumentation",
    openapi_url="/myapi/openapi.json",
    debug=True,
)


async def startup():
    print("DB Connected")
    connection.connect()


app.add_event_handler("startup", startup)

app.include_router(prefix="/api", router=router_tasks)


@app.get("/")
def read_root():
    return {"message": "Welcome app run on port 8000"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
