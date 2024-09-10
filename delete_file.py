import os

if os.path.exists("tomato.txt"):
    os.remove("tomato.txt")
    print("file removed successfully")
else:
    print("file does not exist")