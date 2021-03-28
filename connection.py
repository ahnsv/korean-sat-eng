from elasticsearch_dsl import connections


def create_es_connection():
    try:
        conn = connections.create_connection(
            alias="connection", hosts=["localhost"], timeout=60
        )
        return conn
    except Exception as e:
        raise e
