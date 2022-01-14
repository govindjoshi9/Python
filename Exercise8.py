name = input("Enter your name")
tamp_var = ""
i = 0 
while i < len(name):
    if name[i] not in tamp_var:
        tamp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1