import time
initial = time.time()
#print(initial)
k=0
while(k<45):
    print("THis is harry bhai")
    time.sleep(1)
    k+=1
print("While loop run in",time.time()-initial,"Seconds")
initial2 = time.time()
for i in range(45):
    print("This is harry bhai")

print("for loop run in",time.time()-initial2,"Second")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)