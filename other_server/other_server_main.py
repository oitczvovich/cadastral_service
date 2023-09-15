import random
from asyncio import sleep

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# from app_cadastral.core.db import AsyncSession

app_other = FastAPI(
    title='Сервер принятия решений',
    description="Сервер получает запрос от app_cadastral и генерирует ответ втечение 60 сек и записывает его в базу.",
)


@app_other.get('/need_result')
async def result_cadastral(
        ):
    time = random.randint(1, 60)
    await sleep(time)
    result = random.randint(0, 1)
    return JSONResponse(content={"result": result})


@app_other.get('/ping')
def ping():
    return {'message': 'Сервер работает'}

