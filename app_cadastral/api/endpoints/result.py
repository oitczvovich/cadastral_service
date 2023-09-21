from app_cadastral.core.db import AsyncSessionLocal
from app_cadastral.crud.land_plot import land_plot_crud
from app_cadastral.schemas.land_plot import LandPlotDB

from fastapi import APIRouter

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
