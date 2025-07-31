st="sanga tike dita humps "
str=" niis pakhare jiba"
with open("file_handling/file.txt","w+") as f:
    print(f.write(st))
    f.seek(0)
    print(f.read())