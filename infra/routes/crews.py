from flask import Blueprint, request, jsonify
from infra.repository.crews_repository import CrewsRepository

crew_bp = Blueprint("crews", __name__)


@crew_bp.route("/", methods=["GET"])
def get_crews():
    try:
        crewsRepo = CrewsRepository()
        response = crewsRepo.select()
        crews_list = [
            {
                "id_crew": id_crew,
                "name_crew": name_crew,
                "description_crew": description_crew,
                "process_crew": process_crew,
                "memory_crew": memory_crew,
                "cache_crew": cache_crew,
                "iduser_crew": iduser_crew,
            }
            for id_crew, name_crew, description_crew, process_crew, memory_crew, cache_crew, iduser_crew in response
        ]
        return jsonify(crews_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


@crew_bp.route("/<int:user_id>", methods=["GET"])
def get_crews_by_user_id(user_id):
    try:
        crewsRepo = CrewsRepository()
        response = crewsRepo.selectByUserId(user_id)
        if response:
            crews_list = [
                {
                    "id_crew": id_crew,
                    "name_crew": name_crew,
                    "description_crew": description_crew,
                    "process_crew": process_crew,
                    "memory_crew": memory_crew,
                    "cache_crew": cache_crew,
                    "iduser_crew": iduser_crew,
                }
                for id_crew, name_crew, description_crew, process_crew, memory_crew, cache_crew, iduser_crew in response
            ]
            return crews_list
        else:
            raise ValueError("Equipe não encontrada")
    except ValueError:
        return "", 404
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400
