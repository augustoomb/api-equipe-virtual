from infra.configs.connection import DBConnectionHandler
from infra.entities.users import Users
from sqlalchemy.orm.exc import NoResultFound


class UsersRepository:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Users)
                    # .join(Crews, Users.id_user == Crews.iduser_crew)
                    # .with_entities(
                    #     Users.name_user, Users.email_user, Crews.process_crew
                    # )
                    .with_entities(
                        Users.id_user, Users.name_user, Users.email_user
                    ).all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def selectByEmail(self, email_user):
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Users)
                    .filter(Users.email_user == email_user)
                    # .join(Crews, Users.id_user == Crews.iduser_crew)
                    .with_entities(
                        Users.id_user,
                        Users.name_user,
                        Users.email_user,
                        Users.password_user,
                        # Crews.process_crew,
                    )
                    .all()
                )
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, name_user, email_user, password_user):
        with DBConnectionHandler() as db:
            try:
                data_insert = Users(
                    name_user=name_user,
                    email_user=email_user,
                    password_user=password_user,
                )
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_user):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Users).filter(Users.id_user == id_user).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_user, name_user, email_user, password_user):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Users).filter(Users.id_user == id_user).update(
                    {
                        "name_user": name_user,
                        "email_user": email_user,
                        "password_user": password_user,
                    }
                )
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
