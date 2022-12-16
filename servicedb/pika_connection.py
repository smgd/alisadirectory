def init_pika():
    connection = pika.BlockingConnection()
    channel = connection.channel()

    return connection, channel


def close_pika(connection, channel):
    channel.close()
    connection.close()
