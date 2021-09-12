from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import func
from models.base import Base

class UserAccount(Base):
    __tablename__ = 'user_account'

    id                              = Column(Integer, primary_key=True)
    username                        = Column(String)
    credential                      = Column(String)
    created_at                      = Column(DateTime(timezone=False), server_default=func.now())