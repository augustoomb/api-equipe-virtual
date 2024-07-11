# from infra.repository.tools_repository import ToolsRepository
# from infra.repository.agents_repository import AgentRepository
# from infra.repository.tasks_repository import TaskRepository
# from infra.repository.crews_repository import CrewsRepository
from infra.repository.users_repository import UsersRepository

# repo = ToolsRepository()

# response = repo.update(3, "sheet_generation2")
# print(response)


# =================

# repo = AgentRepository()

# response = repo.select()

# response = repo.insert(
#     "Juca",
#     "Este é um role",
#     "Este é um goal",
#     "Este é um backstory",
#     "gpt-3.5",
#     "aioshdjfoihsadfihas889",
#     True,
#     True,
#     True,
#     1,
# )

# response = repo.delete(2)

# response = repo.update(
#     3,
#     "Jucass",
#     "Este é um role",
#     "Este é um goal",
#     "Este é um backstory",
#     "gpt-4",
#     "aioshdjfoihsadfihas88999",
#     True,
#     True,
#     True,
#     1,
# )

# print(response)


# ==============

# repo = TaskRepository()

# response = repo.select()

# print(response)

# response = repo.insert(
#     "Isso é uma descrição de task",
#     "Isso é uma saida experada de task",
#     False,
#     "arquivosaida.md",
#     1,
# )

# print(response)

# response = repo.delete(2)
# print(response)


# response = repo.update(
#     3,
#     "Isso é uma descrição de task3",
#     "Isso é uma saida experada de task3",
#     True,
#     "arquivosaida3.md",
#     1,
# )

# print(response)


# =====================
# repo = CrewsRepository()

# response = repo.select()

# print(response)

# response = repo.insert("Esse é um process crew", 1, 1, 3, 3)

# print(response)

# response = repo.delete(2)
# print(response)


# response = repo.update(3, "Esse é um process atualizado", 1, 1, 3, 3)

# print(response)


# =====================
repo = UsersRepository()

# response = repo.select()

# print(response)

# response = repo.insert("Nayara", "nay2000@gmail.com", "aioshdfia889786", 3)
# print(response)

# response = repo.delete(2)
# print(response)


response = repo.update(3, "Nayara2", "nay2010@gmail.com", "aioshdfia88978600", 1)
print(response)
