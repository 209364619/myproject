from fdfs_client.client import *


def upload_by_buffer():
    client = Fdfs_client('.\\client.conf')
    print client
    # storages = client.get_storage()
    # print type(storages), storages\


if __name__ == '__main__':
    upload_by_buffer()
