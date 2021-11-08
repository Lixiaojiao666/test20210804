import os
#os.mkdir("testdir")
#print(os.listdir("./"))
#os.removedirs("testdir")
#print(os.getcwd())
os.removedirs("b")

if not os.path.exists("c"):
    os.mkdir("c")
if not os.path.exists("c/test.txt"):
    f=open("c/test.txt","w")
    f.write("hello,my life")
    f.close()


