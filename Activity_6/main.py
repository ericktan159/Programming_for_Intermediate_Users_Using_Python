


f = open("pythonessay.txt", "w")
f.write("I like Python because it's very interesting.")
f = open("pythonessay.txt", "a")
f.write("\nI Plan to learn date vizualization.")
f.write("\nI want to work in the field of data science.")
f.write("\nI Plan to make better world for the future generations.")
f = open("pythonessay.txt", "r")
f.close()

f = open("pythonessay.txt", "r")
print(f.read())
f = open("pythonessay.txt", "r")
print(f.readline())
f = open("pythonessay.txt", "r")
for x in f:
    print(x)
f.close()

#input()

import os

if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")
else:
    print("The file does not exist")
