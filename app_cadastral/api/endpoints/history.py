import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app_cadastral.core.db import get_async_session
from app_cadastral.crud.history import history_crud
from app_cadastral.crud.land_plot import land_plot_crud
from app_cadastral.services.pagination import Pagination

load_dotenv()
PAGINATION = os.getenv('PAGINATION')

router = APIRouter()


@router.get(
    '/',
    response_model_exclude_none=True,
)
async def get_all_historey(
    request: Request,
    session: AsyncSession = Depends(get_async_session),
    page: int = Query(1, ge=0),
    size: int = Query(int(PAGINATION), ge=1, le=100)
):
    all_querys = await land_plot_crud.get_multi(session=session)
    start_index = (page - 1) * size
    end_index = start_index + size
    total_count = len(all_querys)
    results = await history_crud.get_paginated_results(
        start_index,
        end_index,
        session
    )
    pagination = Pagination(request, total_count, page, size)
    next_url = pagination.get_next_url()
    prev_url = pagination.get_prev_url()

    return {
        "results": results,
        "total_count": total_count,
        "page": page,
        "size": size,
        "next_url": next_url,
        "prev_url": prev_url
    }
