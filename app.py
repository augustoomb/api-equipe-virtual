from flask import Flask
from infra.routes.users import user_bp
from infra.routes.crews import crew_bp
from infra.routes.agents import agents_bp
from infra.routes.tasks import tasks_bp
from infra.routes.tools import tools_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(crew_bp, url_prefix="/crews")
app.register_blueprint(agents_bp, url_prefix="/agents")
app.register_blueprint(tasks_bp, url_prefix="/tasks")
app.register_blueprint(tools_bp, url_prefix="/tools")


@app.route("/")
def teste():
    return "Rota de teste"


if __name__ == "__main__":
    app.run()

# from flask import Flask, request, jsonify
# from infra.repository.users_repository import UsersRepository

# app = Flask(__name__)


# @app.route("/")
# def teste():
#     return "Rota de teste"


# @app.route("/users", methods=["GET"])
# def get_users():
#     try:
#         usersRepo = UsersRepository()
#         response = usersRepo.select()
#         # Transformando a lista de tuplas em uma lista de dicionários
#         users_list = [
#             {"id": id, "name": name, "email": email} for id, name, email in response
#         ]

#         return jsonify(users_list)
#     except Exception as e:
#         message = f"Ocorreu um erro: {e}"
#         # logging.error(message)
#         return {"message": message}, 400


# @app.route("/user", methods=["POST"])
# def get_user():
#     try:
#         req_json = request.get_json()
#         email = req_json["email"]

#         usersRepo = UsersRepository()
#         response = usersRepo.selectByEmail(email)

#         if response:
#             users_list = [
#                 {"id": id, "name": name, "email": email, "password": password}
#                 for id, name, email, password in response
#             ]
#             return users_list[0]

#         else:
#             raise ValueError("Usuário não encontrado")

#     except ValueError as ve:
#         return "", 404

#     except Exception as e:
#         message = f"Ocorreu um erro: {e}"
#         return {"message": message}, 400
