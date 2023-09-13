from fastapi import FastAPI

from app.routers import root
from app.routers import health_check
from app.routers import recomendation

app = FastAPI()
app_v1 = FastAPI()

app.mount("/v1", app_v1)
app.include_router(root.router)
app.include_router(health_check.router)


app_v1.include_router(root.router, include_in_schema=False)
app_v1.include_router(health_check.router, include_in_schema=False)
app_v1.include_router(recomendation.router)