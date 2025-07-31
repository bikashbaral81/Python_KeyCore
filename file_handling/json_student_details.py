import json

students=[
{
"name":"abhijit",
"age":23,
"marks":
    {
    "math":70,
    "english":90

    }
},
{
"name":"badal",
"age":22,
"marks":
    {
    "math":75,
    "english":80
    }
}
]


# with open("file_handling/student.json","w") as f:
#     json.dump(students,f,indent=4)
#     

with open("file_handling/student.json","r") as f:
    data=json.load(f)

    for i in data:
        if i["name"]=="abhijit":
           data["age"]=30



with open("file_handling/student.json","w") as f:
    detail=json.dump(data,f,indent=4)
    print(detail)








