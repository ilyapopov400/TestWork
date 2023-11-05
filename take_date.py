'''
Получение данных
'''
import bson

URL = 'DB/dump/sampleDB/sample_collection.bson'


def take_date(file_name: str = URL) -> list:
    with open(file=file_name, mode='rb') as f:
        text_to_read = bson.decode_all(f.read())
    return text_to_read
