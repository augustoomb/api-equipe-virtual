from infra.configs.base import Base
from sqlalchemy import Column, String, Text, Boolean, BigInteger, ForeignKey


class Users(Base):
    __tablename__ = "users"

    id_user = Column(BigInteger, primary_key=True)
    name_user = Column(String)
    email_user = Column(String)
    password_user = Column(String)
