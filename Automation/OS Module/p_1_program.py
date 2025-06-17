import os, platform

print("current working directory = ", os.getcwd())
print("Operating system type = ", os.name)
print("Operating system = ", platform.system())

if os.name == 'nt':
    print("Running in the windows")
elif os.name == 'posix':
    print("Running in the unix, or linux, or mackOS")