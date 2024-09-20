import random
import owner
def itemslist():
    print()
    print("=="*25,"Items list","=="*25)
    fp=open("items.txt")
    print(fp.read())
    fp.close()
    fp=open("items.txt")
    details=fp.readlines()
    fp.close()
    bill=0
    list=[]
    l1=["orderno: ",""]
    list.append(l1)
    while(True):
        number=int(input("choose your dish no: "))
        quantity=int(input("enter the quantity: "))
        
        for i in details:
            i=i.rstrip().split(",")
            if i==['no', 'dish', 'price']:
                pass
            elif number==int(i[0]):
                inner=[]
                inner.append(i[1])
                inner.append(quantity)
                list.append(inner)
                bill+=int(i[2])*quantity
        ch=input("hit a to add more items to order: ")
        if ch=="a":
            continue
        else:
            break
    print()
    print("*"*50,"Your order","*"*50)
    xz=random.randint(100,200)+random.randint(21,40)
    list[0][1]=xz
    for i in range(len(list)):
        if i==0:
            list[i]=tuple(list[i])
            a,b=list[i]
            print(a,b)
            print()
        else:
            print(list[i][0],list[i][1])
            print()

    print(f"-"*45,">","Total Amount: Rs.",bill,"<","-"*45)
    print()
    cnf=input("Enter y to confirm your order: ")
    print()
    if cnf!="y":
        print("*"*25,"Order cancelled!! Login again!!","*"*25)
        print()
    else:
        print("*"*15,"Order will be delivered soon! Thank you Visit agin! ","*"*15)
        print()
        xz=str(xz)
        details=""
        for i in range(len(list)):
            if i==0:
                pass
            else:
                details+=list[i][0]+" "+str(list[i][1])+","
        order=xz+","+details+"\n"
        fp=open("orderslist.txt","a")
        fp.write(order)
        fp.close()   
def update():
    print("-"*65,"X","-"*65)
    print("\t\t\t1.add a new item\n\t\t\t2.delete an item\n\t\t\t3.update the price")
    inp=int(input("enter according to the list: "))
    fp=open("items.txt")
    details=fp.readlines()
    fp.close()
    if inp==1:
        while True:
            flag=0
            num=(input("enter the item no: "))
            for i in details:
                i=i.rstrip().split(",")
                if i[0]==num:
                    flag=1
                    break
            if flag==1:
                print("The item number already exists choose another item number")
                continue
            else:
                name=input("enter the item name: ")
                price=input("enter the item price: ")
                fp=open("items.txt","a")
                content=num+","+name+","+price+"\n"
                fp.write(content)
                fp.close()
                print("-"*20,"Item added successfully!!","-"*20)
                break
        owner.staff()

    elif inp==2:
        while True:
            flag=0
            num=(input("enter the item no: "))
            for i in range(len(details)):
                k=details[i].rstrip().split(",")
                if k[0]==num:
                    details[i]=""
                    flag=1
            if flag==0:
                print("The item number do not exist choose another item number")
                continue
            else:
                print("-"*20,"Item deleted successfully","-"*20)
                fg=open("items.txt","w")
                fg.writelines(details)
                fg.close()
                break
        owner.staff()

    elif inp==3:
        while True:
            flag=0
            num=input("Enter the item no: ")
            for i in range(len(details)):
                k=details[i].rstrip().split(",")
                if k[0]==num:
                    value=input("Enter the updated price of the item: ")
                    details[i]=k[0]+","+k[1]+","+value+"\n"
                    flag=1
            if flag==0:
                print("The item number do not exist choose another item number")
                continue
            else:
                print("-"*20,"price updated successfully","-"*20)
                fp=open("items.txt","w")
                fp.writelines(details)
                fp.close()
                break
        owner.staff()


            

