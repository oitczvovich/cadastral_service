from sqlalchemy import Boolean, Column, String

from core.db import Base


class LandPlot(Base):
    """Модель для участка.
    cadastral_number - кадастровый номер, String(20)
    lat = Column(Decimal(8, 6))
    long = Column(Decimal(9, 6))
    """
    cadastral_number = Column(String(20), nullable=False)
    lat = Column(String(11))
    long = Column(String(11))
    answer_server = Column(Boolean, default=None)
