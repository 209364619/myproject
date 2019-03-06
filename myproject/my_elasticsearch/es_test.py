from elasticsearch5 import Elasticsearch

useIndex = 'tw_user_database_*'
TWEETSINDEX = "tweets_database*"
# host = "192.168.209.113"
# port = "9200"
host = "192.168。8.200"
port = "9201"
es_client = Elasticsearch([{"host": host, "port": port}])
info = es_client.info()

userid = "25073877"
body = {
    "query": {
        "match": {
            "user.id": userid
        }
    }
}

rs = es_client.search(index=TWEETSINDEX, body=body)
print rs
print type(rs)
