from fastapi import APIRouter

from core.db import AsyncSessionLocal
from crud.land_plot import land_plot_crud
from schemas.land_plot import LandPlotDB

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
