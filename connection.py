from elasticsearch_dsl import connections
from elasticsearch import Elasticsearch


def create_es_connection() -> Elasticsearch:
    """ElasticSearch Connection을 만듭니다.

    Raises:
        e: [description]

    Returns:
        ElasticSearch: [ElasticSearch Connection]
    """
    try:
        conn = connections.create_connection(
            hosts=["localhost:9200"], timeout=60
        )
        return conn
    except Exception as e:
        raise e
