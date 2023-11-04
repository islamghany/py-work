from dataclasses import dataclass, field
from typing import List


@dataclass
class User:
    # id is optinal
    name: str
    email: str
    password: str
    created_at: str
    id: int = field(default=0)


class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def find_all(self) -> List[User]:
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = []
        for row in cursor.fetchall():
            users.append(
                User(
                    id=row[0],
                    name=row[1],
                    email=row[2],
                    password=row[3],
                    created_at=row[4],
                )
            )
        return users

    def find_by_id(self, id: int) -> User:
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return User(
            id=row[0],
            name=row[1],
            email=row[2],
            password=row[3],
            created_at=row[4],
        )

    def create(self, user: User) -> User:
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)",
            (user.name, user.email, user.password),
        )
        self.db_connection.commit()
        return user

    def update(self, user: User) -> User:
        cursor = self.db_connection.cursor()
        cursor.execute(
            "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s",
            (user.name, user.email, user.password, user.id),
        )
        self.db_connection.commit()
        return user

    def delete(self, id: int) -> int:
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        self.db_connection.commit()
        return id
