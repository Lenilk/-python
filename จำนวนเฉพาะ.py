a = float(input())

if(a!=1 and a!=2 and a!=3 and a!=5 and a!=7 and a!=13):
    b=a%2
    if(b!=0):
        c=a%3
        if(c!=0):
            d=a%5
            if(d!=0):
                e=a%7
                if(e!=0):
                    f=a%13
                    if(f!=0):
                        print("จำนวนเฉพาะ")
                    else:
                        print("ไม่ใช่จำนวนเฉพาะ")
                else:
                    print("ไม่ใช่จำนวนเฉพาะ")
            else:
                print("ไม่ใช่จำนวนเฉพาะ")     
        else:
            print("ไม่ใช่จำนวนเฉพาะ")
            
    else:
        print("ไม่ใช่จำนวนเฉพาะ")
else:
    print("จำนวนเฉพาะ")