from infra.configs.base import Base
from sqlalchemy import Column, String, Text, Boolean, BigInteger, ForeignKey


class Tasks(Base):
    __tablename__ = "tasks"

    id_task = Column(BigInteger, primary_key=True)
    description_task = Column(Text, nullable=False)
    expected_output_task = Column(Text, nullable=False)
    async_execution_task = Column(Boolean)
    output_file_task = Column(String)
    idcrew_task = Column(BigInteger, ForeignKey("crews.id_crew"))
    # idtool_task = Column(BigInteger, ForeignKey("tools.id_tool"))
