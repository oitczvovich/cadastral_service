import os

import httpx
import asyncio
from dotenv import load_dotenv

from core.db import AsyncSessionLocal
from models.land_plot import LandPlot
from .logging import logger


load_dotenv()
URL_OTHER_SERVER = os.getenv('URL_OTHER_SERVER')


async def send_query(land_plot_id: int, session):
    url = URL_OTHER_SERVER
    retry_interval = 5  # Retry interval in seconds

    async def send_request():
        async with httpx.AsyncClient(timeout=60) as client:
            logger.info(f"Запрос id-{land_plot_id} отправлен на {url}")
            response = await client.get(url)
            if response.status_code == 200:
                result = response.json()['result']
                logger.info(f"Получен ответ {result}, для запроса {land_plot_id}")
                await save_result(land_plot_id, result)
            else:
                logger.info(f"Произошла ошибка при отправке запроса {response.status_code}")
                await asyncio.sleep(retry_interval)
                await send_request()

    try:
        await send_request()
    except Exception as e:
        logger.warning(f"Произошла ошибка при отправке запроса {str(e)}")
        print(f"Произошла ошибка: {str(e)}")


async def save_result(land_plot_id: int, result: int):
    async with AsyncSessionLocal() as session:
        land_plot = await session.get(LandPlot, land_plot_id)
        land_plot.answer_server = result
        logger.info(f"Сохранение результата {result}")
        await session.commit()
        await session.refresh(land_plot)
