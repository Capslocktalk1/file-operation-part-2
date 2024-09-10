import os 
if os.path.exists("Tomato.txt"):
    n = open("Tomato.txt", 'w')
    n.write("Hello i am here.")
    print("modification successful")
    
else:
    nw = open("tomato.txt", 'x')
    nw.write("hello i am here.")
    print("creation and modification successful")