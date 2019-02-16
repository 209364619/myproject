# coding=utf-8
import jieba

str = "中国科学院空天信息研究院"
words = jieba.cut_for_search(str)
for word in words:
    print word
