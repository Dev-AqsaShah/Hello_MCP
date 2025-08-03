with open("data.txt", "r+") as file:
    lines = file.readlines()
    print(lines)  
    file.write("this is a new line.\n")
    print(lines)
    
    
with open("out.txt", "w") as file:
    file.write("this is a new line.\n")
    print(lines)
    