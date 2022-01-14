import os

# print(os.getcwd())
# os.mkdir("Movies")
# print(os.path.exists("Movies"))

# open("file.txt","a").close()
# print(os.listdir())

for item in os.listdir():
    path = os.path.join(os.getcwd(),item)
    print(path)