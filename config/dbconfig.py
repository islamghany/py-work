from dataclasses import dataclass

section_name = "dbconfig"


@dataclass
class DBConfig:
    dbname: str
    user: str
    password: str
    host: str
    port: str


def new_dbconfig(key_val):
    return DBConfig(
        dbname=key_val["dbname"],
        user=key_val["user"],
        password=key_val["password"],
        host=key_val["host"],
        port=key_val["port"],
    )
