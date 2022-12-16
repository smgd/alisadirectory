from .db import get_db
from .pika_connection import init_pika, close_pika


def get_pika_messages(queue_name):
    connection, channel = init_pika()

    for method_frame, properties, body in channel.consume(queue_name):
        yield body

    close_pika(connection, channel)


def consume_appeals():
    for message in get_pika_messages('appeals'):
        # тут сохраняем в базу данных через sqlalchemy
        # то есть берем
        db = get_db()
        # и дальше делаем запрос на сохранение

