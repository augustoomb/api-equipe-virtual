from infra.configs.base import Base
from sqlalchemy import Column, String, Text, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship


class Crews(Base):
    __tablename__ = "crews"

    id_crew = Column(BigInteger, autoincrement="auto", primary_key=True)
    name_crew = Column(String)
    description_crew = Column(Text)
    process_crew = Column(String)
    memory_crew = Column(Boolean)
    cache_crew = Column(Boolean)
    iduser_crew = Column(BigInteger, ForeignKey("users.id_user"))

    # agents = relationship("Agents", back_populates="crew")
