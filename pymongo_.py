#!/usr/bin/python3

import pymongo

#连接服务器
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#查询数据库
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
# print(dblist)

#创建数据库
mydb = myclient['runoobdb']

#创建集合（创建集合后要再插入一个文档，集合才会真正创建）
mycol = mydb["sites"]
# collist = mydb.list_collection_names()
# # collist = mydb.collection_names()
# print(collist)
# if "sites" in collist:  # 判断 sites 集合是否存在
#     print("集合已存在！")

#插入单个文档
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# x = mycol.insert_one(mydict)
# print(x)
# collist = mydb.list_collection_names()
# print(collist)
# if "sites" in collist:  # 判断 sites 集合是否存在
#     print("集合已存在！")
# print(x.inserted_id)

#插入多个文档
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]

x = mycol.insert_many(mylist)
# print(x.inserted_ids)

#插入文档時指定id
# mylist = [
#     {"_id": 1, "name": "RUNOOB", "cn_name": "xiaojun"},
#     {"_id": 2, "name": "Google", "address": "Google"},
#     {"_id": 3, "name": "Facebook", "address": "脸书"},
#     {"_id": 4, "name": "Taobao", "address": "淘宝"},
#     {"_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
#
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

#查询一条数据
x = mycol.find_one()
print(x)

print('------------------------')

#查询所有数据
for x in mycol.find():
    print(x)

print('------------------------')

#指定返回条数
myresult = mycol.find().limit(3)
# 输出结果
for x in myresult:
    print(x)

print('-------------------------')

#查询指定字段的数据
for x in mycol.find({},{ "_id": 0, "name": 1, "alexa": 1, "url": 1}):
    print(x)

print('------------------------')

#设置查询条件
myquery = {"name": "Taobao"} #查找名字为Taobao的文档
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

print('------------------------')

#使用修饰符查询
myquery = {"name": {"$gt": "H"}} #查询名字首字母ascii码大于H的文档
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

print('------------------------')

#使用正则表达式查询
myquery = {"name": {"$regex": "^T"}} #查询名字首字母为T的记录
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# print('------------------------')

#修改匹配到的第一个文档
# myquery = {"alexa": "100"}
# newvalues = {"$set": {"alexa": "123"}}
# mycol.update_one(myquery, newvalues)
# for x in mycol.find():
#     print(x)
#
# print('------------------------')

#修改多个文档
# myquery = {"name": {"$regex": "a"}}
# newvalues = {"$set": {"alexa": "666"}}
# x = mycol.update_many(myquery, newvalues) #查询所有名字中包含a的文档，并将它们的alexa设为666
# print(x.modified_count, "文档已修改") #输出修改的文档数量
# for x in mycol.find():
#     print(x)

print('------------------------')

#指定字段进行排序(升序)
# mydoc = mycol.find().sort("alexa")
# for x in mydoc:
#   print(x)

print('------------------------')

#指定字段进行排序(降)
# mydoc = mycol.find().sort("alexa", -1)
# for x in mydoc:
#   print(x)

print('------------------------')

#删除单条文档
# myquery = {"name": "Taobao"} #删除name为Taobao的文档
# mycol.delete_one(myquery)
# for x in mycol.find():
#     print(x)

print('------------------------')

#删除多个文档
# myquery = {"name": {"$regex": "^F"}}
# x = mycol.delete_many(myquery)
# print(x.deleted_count, "个文档已删除") #输出删除文档的数量
# for x in mycol.find():
#     print(x)

print('------------------------')

#清空集合
# x = mycol.delete_many({})
# print(x.deleted_count, "个文档已删除")
# for x in mycol.find():
#     print(x)

print('------------------------')

#删除集合
# mycol.drop()
# collist = mydb.collection_names()
# print(collist)



