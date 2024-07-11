from infra.configs.connection import DBConnectionHandler

# from infra.entities.tools import Tools
from infra.entities.tasks import Tasks
from sqlalchemy.orm.exc import NoResultFound


class TasksRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Tasks)
                    # .join(Tools, Tasks.idtool_task == Tools.id_tool)
                    .with_entities(
                        Tasks.id_task,
                        Tasks.description_task,
                        Tasks.expected_output_task,
                        Tasks.async_execution_task,
                        Tasks.output_file_task,
                        Tasks.idcrew_task,
                    ).all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(
        self,
        description_task,
        expected_output_task,
        async_execution_task,
        output_file_task,
        # idtool_task,
    ):
        with DBConnectionHandler() as db:
            try:
                data_insert = Tasks(
                    description_task=description_task,
                    expected_output_task=expected_output_task,
                    async_execution_task=async_execution_task,
                    output_file_task=output_file_task,
                    # idtool_task=idtool_task,
                )
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_task):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Tasks).filter(Tasks.id_task == id_task).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(
        self,
        id_task,
        description_task,
        expected_output_task,
        async_execution_task,
        output_file_task,
        # idtool_task,
    ):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Tasks).filter(Tasks.id_task == id_task).update(
                    {
                        "description_task": description_task,
                        "expected_output_task": expected_output_task,
                        "async_execution_task": async_execution_task,
                        "output_file_task": output_file_task,
                        # "idtool_task": idtool_task,
                    }
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
