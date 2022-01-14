# name = "     Gov     ind       "
# dots =  ".........."
# print(name+dots)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# print(name.replace(" ", "")+dots)
# print(name.replace(" ", "__")+dots)
# print(name.find("v"))
# name = "Govind "
# print(name.center(11,"$"))
name = input("Enter a name : ")
print(name.center(len(name)+ 8, "*"))