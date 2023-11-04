from infra.db.repos.users import UserRepository


class Repos:
    user_repo: UserRepository


def init_repos(db_connection):
    repos = Repos()
    repos.user_repo = UserRepository(db_connection)
    return repos
