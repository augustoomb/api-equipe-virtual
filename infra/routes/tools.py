from flask import Blueprint, request, jsonify
from infra.repository.tools_repository import ToolsRepository

tools_bp = Blueprint("tools", __name__)


@tools_bp.route("/", methods=["GET"])
def get_agents():
    try:
        toolsRepo = ToolsRepository()
        response = toolsRepo.select()
        tools_list = [
            {
                "id_tool": id_tool,
                "name_tool": name_tool,
            }
            for id_tool, name_tool in response
        ]
        return jsonify(tools_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


# @tools_bp.route("/<int:crew_id>", methods=["GET"])
# def get_tools_by_crew_id(crew_id):
#     try:
#         toolsRepo = ToolsRepository()
#         response = toolsRepo.select()
#         tools_list = [
#             {
#                 "id_tool": id_tool,
#                 "name_tool": name_tool,
#             }
#             for id_tool, name_tool in response
#         ]
#         return jsonify(tools_list)
#     except Exception as e:
#         message = f"Ocorreu um erro: {e}"
#         return {"message": message}, 400


# @agents_bp.route("/", methods=["GET"])
# def get_agents():
#     try:
#         agentsRepo = AgentsRepository()
#         response = agentsRepo.select()
#         agents_list = [
#             {"id_agent": id_agent, "name_agent": name_agent, "name_crew": name_crew}
#             for id_agent, name_agent, name_crew in response
#         ]
#         return jsonify(agents_list)
#     except Exception as e:
#         message = f"Ocorreu um erro: {e}"
#         return {"message": message}, 400


# @user_bp.route("/email", methods=["POST"])
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
#     except ValueError:
#         return "", 404
#     except Exception as e:
#         message = f"Ocorreu um erro: {e}"
#         return {"message": message}, 400
