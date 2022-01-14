f1 = open("forels.py")

try:
    f = open("does.txt")

# except Exception as e:
#     print(e)

except EOFError as e:
    print("eof error aa gaya ha",e)
except IOError as e:
    print("ioe error aa gaqya ha ",e)

else:
    print("This wil run only if except is not running")

finally:
    print("Run this anyway..")
    f1.close()

print("Important struff")