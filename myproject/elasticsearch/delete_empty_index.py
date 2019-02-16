from elasticsearch5 import Elasticsearch

es_client = Elasticsearch([{"host": "192.168.8.200", "port": "9201"}])

print es_client.info

es_client.
