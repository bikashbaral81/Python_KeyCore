import json

student = {
    "kishan":{
        "age":24,
        "marks":100
        },   
     "mohan":{
        "age":44,
        "marks":80
        }
}

# with open("file_handling/problem.json","w") as f:
#     json.dump(student,f,indent=4)

with open("file_handling/problem.json","r") as f:
    data=json.load(f)

for i in data.values():
    for j in i:
        if ["marks"]==100:
            data["age"]=23

with open("file_handling/problem.json","w") as f:
    result=json.dump(data,f)
    print(result)