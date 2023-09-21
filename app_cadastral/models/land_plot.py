from sqlalchemy import Boolean, Column, String

from app_cadastral.core.db import Base


class LandPlot(Base):
    """Модель для участка.\n
    cadastral_number - кадастровый номер, (String(20), nullable=False)\n
    lat - широта, (String(11), nullable=False)\n
    long - долгота, (String(11), nullable=False)\n
    answer_server - значение от внешнего сервера, (Boolean, default=None).
    """
    cadastral_number = Column(String(20), nullable=False)
    lat = Column(String(11), nullable=False)
    long = Column(String(11), nullable=False)
    answer_server = Column(Boolean, default=None)
