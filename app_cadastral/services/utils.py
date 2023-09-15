import os

import httpx
from dotenv import load_dotenv

from app_cadastral.core.db import AsyncSessionLocal
from app_cadastral.models.land_plot import LandPlot

load_dotenv()
URL_OTHER_SERVER = os.getenv('URL_OTHER_SERVER')


async def send_query(land_plot_id: int, session):
    url = URL_OTHER_SERVER
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.get(url)

        if response.status_code == 200:
            print("Запрос успешно отправлен")
            result = response.json()['result']
            print('result', result)
            await save_result(land_plot_id, result,)

        else:
            print("Произошла ошибка при отправке запроса")


async def save_result(land_plot_id: int, result: int):
    async with AsyncSessionLocal() as session:
        land_plot = await session.get(LandPlot, land_plot_id)
        land_plot.answer_server = result
        await session.commit()
        await session.refresh(land_plot)
