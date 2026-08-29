import random
num=random.randint(1,10)
attempts=0
while True:
 mynum=int(input("my num is:"))
 attempts+=1
 if(num>mynum):
    print("it is low")
 elif(num<mynum):
    print("it is high")
 else:
    print("it is correct")
    break
print("finish")
