from infra.configs.connection import DBConnectionHandler

from infra.entities.users import Users
from infra.entities.agents import Agents

# from infra.entities.tasks import Tasks
from infra.entities.crews import Crews
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import joinedload

import json


class CrewsRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Crews)
                    # .join(Tasks, Crews.idtask_crew == Tasks.id_task)
                    .with_entities(
                        Crews.id_crew,
                        Crews.name_crew,
                        Crews.description_crew,
                        Crews.process_crew,
                        Crews.memory_crew,
                        Crews.cache_crew,
                        Crews.iduser_crew,
                    ).all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def selectByUserId(self, id_user):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Crews)
                    .filter(Users.id_user == id_user)
                    .with_entities(
                        Crews.id_crew,
                        Crews.name_crew,
                        Crews.description_crew,
                        Crews.process_crew,
                        Crews.memory_crew,
                        Crews.cache_crew,
                        Crews.iduser_crew,
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
        name_crew,
        description_crew,
        process_crew,
        memory_crew,
        cache_crew,
        iduser_crew,
    ):
        with DBConnectionHandler() as db:
            try:
                data_insert = Crews(
                    name_crew=name_crew,
                    description_crew=description_crew,
                    process_crew=process_crew,
                    memory_crew=memory_crew,
                    cache_crew=cache_crew,
                    iduser_crew=iduser_crew,
                )
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_crew):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Crews).filter(Crews.id_crew == id_crew).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(
        self,
        id_crew,
        name_crew,
        description_crew,
        process_crew,
        memory_crew,
        cache_crew,
        iduser_crew,
    ):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Crews).filter(Crews.id_crew == id_crew).update(
                    {
                        "name_crew": name_crew,
                        "description_crew": description_crew,
                        "process_crew": process_crew,
                        "memory_crew": memory_crew,
                        "cache_crew": cache_crew,
                        "iduser_crew": iduser_crew,
                    }
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
