from infra.configs.base import Base
from sqlalchemy import Column, String, Text, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship


class Agents(Base):
    __tablename__ = "agents"

    id_agent = Column(BigInteger, autoincrement="auto", primary_key=True)
    name_agent = Column(String, nullable=False)
    role_agent = Column(String, nullable=False)
    goal_agent = Column(Text)
    backstory_agent = Column(Text)
    llm_agent = Column(String, default="gpt-4")
    llm_key_agent = Column(String)
    allow_delegation_agent = Column(Boolean)
    verbose_agent = Column(Boolean)
    memory_agent = Column(Boolean)
    idcrew_agent = Column(BigInteger, ForeignKey("crews.id_crew"))

    # crew = relationship("Crews", back_populates="agents")

    # def __repr__(self):
    #     return f"Agents (id_agent={ self.id_agent }, name_agent={ self.name_agent })"
