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
    
with open("file_handling/student.json","r") as f:
    data=json.load(f)

student={}

student["name"]="deepak"
student["age"]=23
student["marks"]={"math":90,"english":45}



print(student)
data.append(student)

with open("file_handling/student.json","w") as f:
     result=json.dump(data,f,indent=4)
     print(result)