import p_1_program
with open("note.txt", "w") as file:
    file.write("Hello programmers.\n")
    file.write("How are you all programmers\n")
    file.write("I Love python scripting\n")


a = p_1_program.customFile("all")
print(a)

lines = [
    "line1 : I play football\n",
    "line2 : I play cricket\n",
    "line3 : I play chess\n",
]
with open("note.txt", "a") as file:
    file.write("Hi i am new line newly adding.\n")
    file.writelines(lines)

a = p_1_program.customFile("lines")
for i in a:
    print(i, end=" ")
