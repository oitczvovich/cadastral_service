import re
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class LandPlotBase(BaseModel):
    """ Базовая схема для участка."""
    cadastral_number: Optional[str]
    lat: Optional[str]
    long: Optional[str]
    answer_server: Optional[bool]

    class Config:
        extra = Extra.forbid


class LandPlotCreate(BaseModel):
    """Модель для создания запрос земельного участка."""
    cadastral_number: str = Field(
        ..., min_length=13, max_length=17,
        title='Кадастровый номер',
        description='Кадастровый номера в формате 00:00:0000000:00'
    )
    lat: str = Field(
        ...,
        min_length=7,
        max_length=11,
        title='Широта',
        description='Широта в формате от -90 до 90. c 6 знаками после запятой'
    )
    long: str = Field(
        ...,
        min_length=7,
        max_length=11,
        title='Долгота',
        description=(
            'Долгота в формате от -180 до 180. c 6 знаками после запятой'
        )
    )

    @validator('*')
    def field_is_empty(cls, field: str):
        """Прроверка в поле наличия данных."""
        if field.isspace() or field == '' or field is None:
            raise ValueError(
                'Поле не может быть пустым.'
            )
        return field

    @validator('cadastral_number')
    def check_cadastral_number(cls, field: str):
        """Проверка кадастрового номера на соответсвие формату."""
        pattern = r'^\d{2}:\d{2}:\d{7}:\d{2}$'
        match = re.match(pattern, field)
        if not match:
            raise ValueError(
                'Кадастровый номера должен быть в формате 00:00:0000000:00'
            )
        return field

    @validator('lat')
    def validate_latitude(lat: str):
        """Проверка кадастрового номера на соответсвие формату."""
        pattern = r'^-?\d{1,2}\.\d{6}$'
        match = re.match(pattern, lat)
        if match:
            lat_float = float(lat)
            if -90 <= lat_float <= 90:
                return lat
        raise ValueError('Не правильный формат данных широты.')

    @validator('long')
    def validate_longitude(long: float):
        """Проверка кадастрового номера на соответсвие формату."""
        pattern = r'^-?\d{1,3}\.\d{6}$'
        match = re.match(pattern, long)
        if match:
            lat_float = float(long)
            if -180 <= lat_float <= 180:
                return long
        raise ValueError('Не правильный формат данных долготы.')


class LandPlotDB(LandPlotBase):
    """Схема с данными из БД."""
    id: int

    class Config:
        orm_mode = True
