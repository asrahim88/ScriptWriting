import os, platform

# print(os)
# print(dir(os))
# print(os.system)
# print(os.name)
# print()
# print(os.getcwd())
# print(platform.system())
# os.chdir("G:")
# newdir = os.getcwd()
# print(os.listdir())
# os.chdir("..\C programming Projects")
# print(os.getcwd())
# print(len(os.listdir()))
print(os.getcwd())
os.chdir("C:/Users/Asus/Desktop")
print(os.getcwd())
print(len(os.listdir()))
items = os.listdir()

for i in items:
    print(i)

os.chdir("E:\Python Automation Scripts\Python Script Writing\Automation\OS Module")
print(os.getcwd())
