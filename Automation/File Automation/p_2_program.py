import p_1_program
with open("note.txt", "w") as file:
    file.write("Hello programmers.\n")
    file.write("How are you all programmers\n")
    file.write("I Love python scripting\n")

a = p_1_program.customFile("all")
print(a)