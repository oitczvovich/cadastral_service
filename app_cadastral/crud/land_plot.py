from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.crud.base import CRUDBase
from app_cadastral.models import LandPlot
from app_cadastral.schemas.land_plot import LandPlotBase, LandPlotCreate


class CRUDLandPlot(CRUDBase):
    pass

land_plot_crud = CRUDLandPlot(LandPlot)

