from flask import Blueprint, request, jsonify
from infra.repository.tasks_repository import TasksRepository

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/", methods=["GET"])
def get_agents():
    try:
        tasksRepo = TasksRepository()
        response = tasksRepo.select()
        tasks_list = [
            {
                "id_task": id_task,
                "description_task": description_task,
                "expected_output_task": expected_output_task,
                "async_execution_task": async_execution_task,
                "output_file_task": output_file_task,
                "idcrew_task": idcrew_task,
            }
            for id_task, description_task, expected_output_task, async_execution_task, output_file_task, idcrew_task in response
        ]
        return jsonify(tasks_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


# @tasks_bp.route("/<int:crew_id>", methods=["GET"])
# def get_agents_by_crew_id(crew_id):
#     try:
#         agentsRepo = AgentsRepository()
#         response = agentsRepo.selectByCrewId(crew_id)
#         agents_list = [
#             {
#                 "id_agent": id_agent,
#                 "name_agent": name_agent,
#                 "role_agent": role_agent,
#                 "goal_agent": goal_agent,
#                 "backstory_agent": backstory_agent,
#                 "llm_agent": llm_agent,
#                 "llm_key_agent": llm_key_agent,
#                 "allow_delegation_agent": allow_delegation_agent,
#                 "verbose_agent": verbose_agent,
#                 "memory_agent": memory_agent,
#                 "idcrew_agent": idcrew_agent,
#             }
#             for id_agent, name_agent, role_agent, goal_agent, backstory_agent, llm_agent, llm_key_agent, allow_delegation_agent, verbose_agent, memory_agent, idcrew_agent in response
#         ]
#         return jsonify(agents_list)
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
