import urllib2
import json
import requests

data = json.dumps({"username": "zhaoshuang", "password": "admin1234"})
data = 'search_type=normal&normal_search_condition=%7B%22search_fields%22%3A%5B%22text%22%5D%2C%22lang_type%22%3A%5B%22all%22%5D%2C%22verified%22%3A%22%22%2C%22location%22%3A%22all%22%2C%22retweeted%22%3A%22all%22%2C%22up_label%22%3A%5B%5D%7D&advanced_search_condition=%7B%22verified%22%3A%22%22%2C%22location%22%3A%22all%22%2C%22retweeted%22%3A%22all%22%2C%22up_label%22%3A%5B%5D%2C%22descript_keywords%22%3A%22%22%2C%22name_keys%22%3A%22%22%2C%22screen_name_keys%22%3A%22%22%2C%22location_keys%22%3A%22%22%2C%22label_keys%22%3A%22%22%2C%22text_keywords%22%3A%22%22%2C%22tw_labels_keys%22%3A%22%22%2C%22tw_location_keys%22%3A%22%22%2C%22country_keys%22%3A%22%22%2C%22descript_match_type%22%3A%22match%22%2C%22name_match_type%22%3A%22match%22%2C%22screen_name_match_type%22%3A%22match%22%2C%22location_match_type%22%3A%22match%22%2C%22label_match+type%22%3A%22match%22%2C%22text_match_type%22%3A%22match%22%2C%22tw_labels_match_type%22%3A%22match%22%2C%22tw_location_match_type%22%3A%22match%22%2C%22country_match_type%22%3A%22match%22%7D&keywords=%E4%B8%AD%E5%9B%BD&match_type=match&start_num=0&total_num=10&sort_by=&asc_or_dec=asc&timestamp=%7B%22start_time%22%3A946742460%2C%22end_time%22%3A1551678660%7D'
try:
    req = urllib2.Request('http://192.168.8.200:8002/twitter_index/', data,
                          {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
    f = urllib2.urlopen(req)
    response = f.read()
    print response
    f.close()
except urllib2.URLError, e:
    print e


def requests_test():
    import json
    data = {"filename": "1556005593.txt"}
    rsp = requests.post('http://192.168.8.200:8000/get_entity/', json.dumps(data, ensure_ascii=False))
    print(rsp.text)


if __name__ == '__main__':
    requests_test()
