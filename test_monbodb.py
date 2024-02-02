from pymongo import MongoClient

# 방법1 - URI
mongodb_URI = "mongodb+srv://root:1234@ubion9.f9lapgm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_URI)
# print(client.list_database_names())

# 방법2 - HOST, PORT
# client = MongoClient(host='localhost', port=27017)

# database => schema
db = client.ubion9

# table => collections
data = db.mydata

# data.insert_one({
#     "username" : 'kim',
#     'password' : '1234'
# })

# data.insert_one({
#     "username" : 'park',
#     'password' : '5678'
# })

# select * from mydata
# cursor = data.find()

# username으로 검색
# cursor = data.find({'username':'kim'})
# print(list(cursor)) # [] 형태

# cursor = data.find_one({'username':'kim'})
# print(cursor) # {} 형태

data = db.users
cursor_1 = data.find_one({'email' : '1@naver.com'})
if cursor_1 == None:
    print('SS')
else:
    print(cursor_1) # {} 형태

# 연결 종료
client.close()