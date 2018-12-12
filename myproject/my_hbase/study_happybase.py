#!coding=utf-8
import happybase

conn = happybase.Connection("10.10.10.50", 9090)
print conn.tables()
