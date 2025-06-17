def customFile(func):
    with open("note.txt", "r") as file:
        if func =="all":
            return file.read()
        elif func == "line":
            return file.readline()
        elif func == "lines":
            return file.readlines()
        
allCharacter = customFile("all")
print("Total length = ",len(allCharacter),allCharacter)
allCharacter = customFile("line")
print("Total length = ",len(allCharacter), allCharacter)
allCharacter = customFile("lines")
print("Total length = ",len(allCharacter),allCharacter)

    