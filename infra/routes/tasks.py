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
                "name_task": name_task,
                "description_task": description_task,
                "status_task": status_task,
                "expected_output_task": expected_output_task,
                "async_execution_task": async_execution_task,
                "output_file_task": output_file_task,
                "idcrew_task": idcrew_task,
            }
            for id_task, name_task, description_task, status_task, expected_output_task, async_execution_task, output_file_task, idcrew_task in response
        ]
        return jsonify(tasks_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


@tasks_bp.route("/<int:crew_id>", methods=["GET"])
def get_tasks_by_crew_id(crew_id):
    try:
        tasksRepo = TasksRepository()
        response = tasksRepo.selectByCrewId(crew_id)
        tasks_list = [
            {
                "id_task": id_task,
                "name_task": name_task,
                "description_task": description_task,
                "status_task": status_task,
                "expected_output_task": expected_output_task,
                "async_execution_task": async_execution_task,
                "output_file_task": output_file_task,
                "idcrew_task": idcrew_task,
            }
            for id_task, name_task, description_task, status_task, expected_output_task, async_execution_task, output_file_task, idcrew_task in response
        ]
        return jsonify(tasks_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


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
