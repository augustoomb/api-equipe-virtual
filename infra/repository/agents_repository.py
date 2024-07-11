from infra.configs.connection import DBConnectionHandler

from infra.entities.crews import Crews
from infra.entities.agents import Agents
from sqlalchemy.orm.exc import NoResultFound


class AgentsRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Agents)
                    # .join(Crews, Crews.id_crew == Agents.idcrew_agent)
                    .with_entities(
                        Agents.id_agent,
                        Agents.name_agent,
                        Agents.role_agent,
                        Agents.goal_agent,
                        Agents.backstory_agent,
                        Agents.llm_agent,
                        Agents.llm_key_agent,
                        Agents.allow_delegation_agent,
                        Agents.verbose_agent,
                        Agents.memory_agent,
                        Agents.idcrew_agent,
                    ).all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def selectByCrewId(self, crew_id):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Agents)
                    .filter(Agents.idcrew_agent == crew_id)
                    # .join(Crews, Crews.id_crew == Agents.idcrew_agent)
                    .with_entities(
                        Agents.id_agent,
                        Agents.name_agent,
                        Agents.role_agent,
                        Agents.goal_agent,
                        Agents.backstory_agent,
                        Agents.llm_agent,
                        Agents.llm_key_agent,
                        Agents.allow_delegation_agent,
                        Agents.verbose_agent,
                        Agents.memory_agent,
                        Agents.idcrew_agent,
                    )
                    .all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(
        self,
        name_agent,
        role_agent,
        goal_agent,
        backstory_agent,
        llm_agent,
        llm_key_agent,
        allow_delegation_agent,
        verbose_agent,
        memory_agent,
        idcrew_agent,
    ):
        with DBConnectionHandler() as db:
            try:
                data_insert = Agents(
                    name_agent=name_agent,
                    role_agent=role_agent,
                    goal_agent=goal_agent,
                    backstory_agent=backstory_agent,
                    llm_agent=llm_agent,
                    llm_key_agent=llm_key_agent,
                    allow_delegation_agent=allow_delegation_agent,
                    verbose_agent=verbose_agent,
                    memory_agent=memory_agent,
                    idcrew_agent=idcrew_agent,
                )
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_agent):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Agents).filter(Agents.id_agent == id_agent).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(
        self,
        id_agent,
        name_agent,
        role_agent,
        goal_agent,
        backstory_agent,
        llm_agent,
        llm_key_agent,
        allow_delegation_agent,
        verbose_agent,
        memory_agent,
        idcrew_agent,
    ):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Agents).filter(Agents.id_agent == id_agent).update(
                    {
                        "name_agent": name_agent,
                        "role_agent": role_agent,
                        "goal_agent": goal_agent,
                        "backstory_agent": backstory_agent,
                        "llm_agent": llm_agent,
                        "llm_key_agent": llm_key_agent,
                        "allow_delegation_agent": allow_delegation_agent,
                        "verbose_agent": verbose_agent,
                        "memory_agent": memory_agent,
                        "idcrew_agent": idcrew_agent,
                    }
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
