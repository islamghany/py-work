from dataclasses import dataclass
from infra.db.repos.users import UserRepository, User


class UserHandler:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all(self):
        return self.user_repository.find_all()

    def get_by_id(self, id: int):
        return self.user_repository.find_by_id(id)

    def create(self, user: User):
        return self.user_repository.create(user)

    def update(self, user: User):
        return self.user_repository.update(user)

    def delete(self, id: int):
        return self.user_repository.delete(id)
