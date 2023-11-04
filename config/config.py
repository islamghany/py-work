from configparser import ConfigParser
from dataclasses import dataclass
import config.dbconfig as dbconfig


@dataclass
class Config:
    dbconfig: dbconfig.DBConfig


def init_config():
    parser = ConfigParser()
    parser.read("./config/config.ini")
    print(parser.sections())
    DBConfig = None
    if parser.has_section(dbconfig.section_name):
        key_val = dict(parser.items(dbconfig.section_name))
        DBConfig = dbconfig.new_dbconfig(key_val)

    return Config(dbconfig=DBConfig)
