from fastadmin import fastapi_app as admin_app
from fastapi import APIRouter, FastAPI

from app_cadastral.api.endpoints import (history_router,  # admin_router
                                         ping_router, query_router,
                                         result_router)

main_router = APIRouter()
main_router.include_router(
    query_router, prefix='/query', tags=['Query']
)
main_router.include_router(
    result_router, prefix='/result', tags=['Result']
)
main_router.include_router(
    ping_router, prefix='/ping', tags=['Ping-service']
)
main_router.include_router(
    history_router, prefix='/history', tags=['History']
)
# main_router.include_router(admin_app)
