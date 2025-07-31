# json file handling(JAVASCRIPT OBJECT NOTATION)

import json 

student={
    "name":"kartik","age":25,"marks":{"math":80,"english":90}}

# json_str=json.dumps(student,indent=4)
# print(json_str)

# with open("file_handling/json.json","w")as f:    #json WRITE Operation
#     json.dump(student,f,indent=4)


#with open("file_handling/json.json","r")as f:       #json READ Operation      
#    json.load(f)


# with open("file_handling/json.json","r")as f:
#     data=f.read()
#     new_data=json.loads(data)
#     print(new_data)


# with open("file_handling/json.json","r")as f:             
#    data=json.load(f)
#    for i in data:
#       print (data[i])

with open("file_handling/json.json","r")as f:             
    data=json.load(f)
    for key,value in data.items():
        print(f"subject={key},marks={value}")
    data["age"]=30

with open("file_handling/json.json","w")as f:    
    json.dump(data,f)

