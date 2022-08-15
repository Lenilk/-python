a = int(input())
list = []
for i in range(a):
    i+=1
    b=a%i
    if(b==0):
        list.append(i)
print(list)
if(len(list)==2):
    print("เป็นจำนวนเฉพาะ")
else:
    print("ไม่เป็นจำนวนเฉพาะ")
