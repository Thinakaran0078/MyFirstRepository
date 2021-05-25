import pymongo
import sys
import logging

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["TestDB"]

collection = db["tblEmployee"]

#col2 = db["DelDB"]

#collection.insert_one(
#    {"name": "Student3", "rollno": "003", "subjects": ["math", "english", "dbms"], "marks": "99", "passed": "False"}
#)


#collection.update_many(
#    {"marks": {"$gt": "35"}},
#    {"$set": {"passed": "True"}}
#)

# collection.update_many(
#     {},
#     {"$set":
#         {
#             "Address": "value"
#         }
#     },
#     # don't insert if no document found
#     upsert=False,
#     array_filters=None
# )

#for x in collection.find().limit(2):
#    print(x)

# Before Creating index
# index_list = sorted(list(collection.index_information()))
# print("Before Creating index")
# print(index_list)
#
# # Creating index
# collection.create_index("rollno", unique=True)
#
# # After Creating index
# index_list = sorted(list(collection.index_information()))
# print("\nAfter Creating index")
# print(index_list)

# logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#     datefmt='%d-%m-%Y:%H:%M:%S',
#     level=logging.DEBUG,
#     filename='logs.txt')
#
#
# logger = logging.getLogger("mylogger")
#
#
# record = {"rollno": "002",
#           "name": "Dhina",
#           "marks": "100"}
# try:
#     collection.insert_one(record)
# except Exception as err:
#     logger.error(msg=(str(err)))

collection.drop_index("rollno_1")