import os

def deleteFile():
    # if os.path.exists("note.txt"):
    #     os.remove("note.txt")
    #     return "Successfully Deleted!"
    # else:
    #     return "This file is not found"
    try:
        os.remove("note.txt")
        return "successfully delete the file"
    except FileNotFoundError:
        return "any file doesn't found"
        
    
def deleteFolder():
    try:
        os.rmdir("myfolder")
        return "Successfully deleted folder."
    except:
        return "Any folder not found."
    
delete = deleteFile()
print(delete)

print(deleteFolder())