import json
from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.crud.base import CRUDBase
from app_cadastral.models import LandPlot


class CRUDHistory(CRUDBase):

    async def get_paginated_results(
        self,
        start_index: int,
        end_index: int,
        session: AsyncSession
    ) -> list:
        query = select(LandPlot).offset(start_index).limit(end_index - start_index)
        result = await session.execute(query)
        results = result.scalars().all()

        return results


history_crud = CRUDHistory(LandPlot)
