# ！coding=utf-8
my_list = ['一', '二', '三']

# 查找根据下标查找list
for i in range(len(my_list)):
    print i
    print my_list[i]

# 根据元素查找所在list的下标
print "根据元素查找所在list的下标"
print my_list.index('一')
target = '六'
if target in my_list:
    print target, '在list中'
else:
    print target, "不在list中"


# str 内容list转化为整形
def test():
    l1 = ["231231", "", "23213123"]
    for item in l1:
        if not item == "":
            rs = int(item)
            print rs


if __name__ == '__main__':
    test()
