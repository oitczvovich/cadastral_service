from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.core.db import AsyncSessionLocal
from app_cadastral.crud.base import CRUDBase
from app_cadastral.models.land_plot import LandPlot
from app_cadastral.schemas.land_plot import LandPlotBase, LandPlotCreate


class CRUDResult(CRUDBase):
    pass


result_crud = CRUDResult(CRUDResult)
