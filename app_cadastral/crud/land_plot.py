from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import LandPlot


class CRUDLandPlot(CRUDBase):
    pass


land_plot_crud = CRUDLandPlot(LandPlot)
