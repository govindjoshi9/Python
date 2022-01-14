name, char = input("Enter a name and any charecter ").split(",")
print(len(name))
#print(char.count(""))
print(name.strip().lower().count(char.strip().lower()))