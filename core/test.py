#Create my own file to debug stuff
import requests
import json
BASE="http://localhost:5000/"
# res=requests.get(BASE+'student/assignments',headers={'X-principal':json.dumps({"user_id":1,"student_id":1})})
# print(json.dumps(res.json(),indent=2))

# res=requests.post(BASE+'/student/assignments',headers={'X-Principal': json.dumps({
#             'student_id': 1,
#             'user_id': 1
#         })},json={'content':'This is a random test'})
# print(json.dumps(res.json(),indent=2))

res=requests.get(BASE+'principal/teachers',headers={'X-principal':json.dumps({"user_id":5,"principal_id":1})})
print(json.dumps(res.json(),indent=2))
