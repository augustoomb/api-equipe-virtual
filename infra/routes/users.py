from flask import Blueprint, request, jsonify
from infra.repository.users_repository import UsersRepository

user_bp = Blueprint("users", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    try:
        usersRepo = UsersRepository()
        response = usersRepo.select()
        users_list = [
            {"id": id, "name": name, "email": email} for id, name, email in response
        ]
        return jsonify(users_list)
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400


@user_bp.route("/email", methods=["POST"])
def get_user():
    try:
        req_json = request.get_json()
        email = req_json["email"]
        usersRepo = UsersRepository()
        response = usersRepo.selectByEmail(email)
        if response:
            users_list = [
                {"id": id, "name": name, "email": email, "password": password}
                for id, name, email, password in response
            ]
            return users_list[0]
        else:
            raise ValueError("Usuário não encontrado")
    except ValueError:
        return "", 404
    except Exception as e:
        message = f"Ocorreu um erro: {e}"
        return {"message": message}, 400
