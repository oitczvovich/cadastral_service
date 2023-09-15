from typing import List

from fastapi import APIRouter, Depends

from app_cadastral.core.db import AsyncSessionLocal, get_async_session
from app_cadastral.crud.land_plot import land_plot_crud
# from app_cadastral.core.user import current_superuser, current_user
from app_cadastral.models import User
from app_cadastral.schemas.land_plot import LandPlotDB

router = APIRouter()


@router.get(
    '/{obj_id}',
    response_model=LandPlotDB,
)
async def get_result_query(
    obj_id: int,

):
    async with AsyncSessionLocal() as session:
        res = await land_plot_crud.get(obj_id, session=session)
        return res
