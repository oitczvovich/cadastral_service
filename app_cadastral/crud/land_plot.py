from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.crud.base import CRUDBase
from app_cadastral.models import LandPlot


class CRUDLandPlot(CRUDBase):
    pass


land_plot_crud = CRUDLandPlot(LandPlot)
