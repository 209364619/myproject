from fdfs_client.client import *

client = Fdfs_client('F:\\python workspace\\myproject\\myproject\\my_fdfs\\client.conf')
print client
ret = client.upload_by_filename('F:\\python workspace\\myproject\\myproject\\my_fdfs\\client.conf')

print ret
