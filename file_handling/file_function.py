def file_operation():

    num_of_words=0
    num_of_lins=0
    num_of_chars=0
    with open("file_handling/file.txt","r") as f:
        for line in f:
            num_of_words=len(line.split())
            num_of_lins+=1
            num_of_chars=len(line)
    return num_of_chars,num_of_lins,num_of_words
print(file_operation())