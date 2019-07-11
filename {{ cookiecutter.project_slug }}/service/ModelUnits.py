from sqlalchemy import Column, Integer, BigInteger, VARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates


Base = declarative_base()


class ModelUnits(Base):
    __tablename__ = 'change_order_units'

    Id = Column(BigInteger, primary_key=True)
    StoreNum = Column(Integer)
    ServiceDay = Column(VARCHAR)
    ServicerName = Column(VARCHAR)
    ServiceStarting = Column(Date)
    ServiceEnding = Column(Date)

    @validates('ServiceDay')
    def validate_service_day(self, key, value):
        value = str(value).lower()
        assert value in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        return value
