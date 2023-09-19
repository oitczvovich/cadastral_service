import asyncio

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud.land_plot import land_plot_crud
from schemas.land_plot import LandPlotCreate, LandPlotDB
from services.utils import send_query

router = APIRouter()


@router.post(
        '/',
        response_model=LandPlotDB,
        response_model_exclude_none=True,
)
async def create_new_land_plot(
        obj_in: LandPlotCreate,
        session: AsyncSession = Depends(get_async_session),
):
    new_land_plot = await land_plot_crud.create(obj_in, session=session)
    asyncio.create_task(send_query(new_land_plot.id, session=session))
    return new_land_plot
