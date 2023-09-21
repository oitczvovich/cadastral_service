from app_cadastral.api.endpoints import (history_router, ping_router,
                                         query_router, result_router)

from fastapi import APIRouter

main_router = APIRouter(prefix='/api')

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
