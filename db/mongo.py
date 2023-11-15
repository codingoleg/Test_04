import pymongo

import config

default_rows = [
    {"date": "2023-10-10", "phone_num": "70000000000", "email": "email000000@mail.ru", "text": "0 text"},
    {"date": "2023-10-10", "phone_num": "70000000000", "email": "email111111@mail.ru", "text": "1 text"},
    {"date": "2023-10-11", "phone_num": "71111111111", "email": "email111111@mail.ru", "text": "1 text"},
    {"date": "2023-10-12", "phone_num": "73333333333", "email": "email222222@mail.ru", "text": "2 text"},
    {"date": "2023-10-13", "phone_num": "73333333333", "email": "email333333@mail.ru", "text": "3 text"},
    {"date": "2023-10-14", "phone_num": "74444444444", "email": "email444444@mail.ru", "text": "4 text"}
]

db_client = pymongo.MongoClient(f'mongodb://{config.DB_HOST}:{config.DB_PORT}/')

current_db = db_client[config.DB_NAME]
collection = current_db[config.DB_COLLECTION_NAME]
collection.insert_many(default_rows)
