import psycopg2
from config import config
from infra.db.repos.repos import init_repos
from infra.db.repos.users import User
from handlers.user import UserHandler
import os

Config = config.init_config()
db_connection = None
try:
    db_connection = psycopg2.connect(
        host=Config.dbconfig.host,
        port=Config.dbconfig.port,
        user=Config.dbconfig.user,
        password=Config.dbconfig.password,
        dbname=Config.dbconfig.dbname,
    )
except Exception as e:
    print(e)
    os.exit(1)

repos = init_repos(db_connection)

# Create
user = User(
    id=12, name="John Doe", email="example", password="123456", created_at="2021-01-01"
)

user_handler = UserHandler(repos.user_repo)
try:
    # user_handler.create(user)
    user = user_handler.get_by_id(1)
    print("User created", user)
except Exception as e:
    print(e)


db_connection.close()
