def dispatch():
    print("="*40,"Live orders","="*40)
    fp=open("orderslist.txt")
    details=fp.readlines()
    fp.close()
    for i in range(len(details)):
        print(details[i])
    while True:
        l1=[]
        flag=0
        inp=(input("enter the order no: "))
        for i in range(len(details)):
            k=details[i].rstrip().split(",")
            if k[0]==inp:
                flag=1
            else:
                l1.append(details[i])
        if flag==0:
            print("The order number do not exist choose another item number")
            continue
        else:
            fp=open("orderslist.txt","w")
            fp.writelines(l1)
            fp.close()
            print('-'*20,"Order number ",inp," dispatched!!!","-"*20)
            break


 