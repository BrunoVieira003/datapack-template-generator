import os
import sqlite3
from DBManager import DBManager
from pack_builder import Pack

db_manager = DBManager("data/data.db")

version_translation = {"1.16": 6, "1.15": 5, "1.14": 4}

name = input("Datapack name: ")
namespace = input("Datapack namespace: ")
desc = input("Datapack description(optional): ")
version = input("Datapack version: ")

db_manager.insert(name, namespace, desc, version_translation[version])

if input("Generate?[y/n]: ").lower() == "y":
    pack = Pack(db_manager.get_pack(name))
    pack.generate("output")

db_manager.clear_table("datapacks")
db_manager.close()