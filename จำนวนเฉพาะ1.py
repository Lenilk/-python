while(1<3):
    a=int(input())
    b=a%2
    c=a%3
    d=a%5
    e=a%7
    f=a%13
    if(a!=1 and a!=2 and a!=3 and a!=5 and a!=7 and a!=13):
        if(b!=0 and c!=0 and d!=0 and e!=0 and f!=0):
            print("จำนวนเฉพาะ")
        else:
            print("ไม่ใช่จำนวนเฉพาะ")
    else:
        print("จำนวนเฉพาะ")
6