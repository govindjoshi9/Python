import  pickle

# car = ["Audi", "Bmw", "Maruti suzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(car,fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))