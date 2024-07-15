from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey


class Tools(Base):
    __tablename__ = "tools"

    id_tool = Column(BigInteger, primary_key=True)
    name_tool = Column(String, nullable=False)

    # def __repr__(self):
    #     return f"Tools (id_tool={ self.id_tool }, name_tool={ self.name_tool })"
