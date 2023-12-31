import random
from asyncio import sleep

from fastapi.responses import JSONResponse

from fastapi import FastAPI

# from app_cadastral.core.db import AsyncSession

app = FastAPI(
    title='Сервер принятия решений',
    description="Сервер получает запрос от app_cadastral и генерирует ответ втечение 60 сек и записывает его в базу.",
)


@app.get('/need_result')
async def result_cadastral(
        ):
    time = random.randint(1, 60)
    await sleep(time)
    result = random.randint(0, 1)
    
    return JSONResponse(content={"result": result})


@app.get('/ping')
def ping():
    return {'message': 'Сервер работает'}
