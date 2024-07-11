# from infra.configs.connection import DBConnectionHandler
# from infra.entities.tools import Tools
# from sqlalchemy.orm.exc import NoResultFound


# class ToolsRepository:
#     def select(self):
#         with DBConnectionHandler() as db:
#             try:
#                 data = db.session.query(Tools).all()
#                 return data
#             except NoResultFound:
#                 return None
#             except Exception as exception:
#                 db.session.rollback()
#                 raise exception

#     def insert(self, name_tool):
#         with DBConnectionHandler() as db:
#             try:
#                 data_insert = Tools(name_tool=name_tool)
#                 db.session.add(data_insert)
#                 db.session.commit()
#             except Exception as exception:
#                 db.session.rollback()
#                 raise exception

#     def delete(self, id_tool):
#         with DBConnectionHandler() as db:
#             try:
#                 db.session.query(Tools).filter(Tools.id_tool == id_tool).delete()
#                 db.session.commit()
#             except Exception as exception:
#                 db.session.rollback()
#                 raise exception

#     def update(self, id_tool, name_tool):
#         with DBConnectionHandler() as db:
#             try:
#                 db.session.query(Tools).filter(Tools.id_tool == id_tool).update(
#                     {"name_tool": name_tool}
#                 )
#                 db.session.commit()
#             except Exception as exception:
#                 db.session.rollback()
#                 raise exception
