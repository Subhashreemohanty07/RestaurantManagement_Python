import items
import orders
def staff():
    while(True):
        print("-"*25,"What do you want to do?","-"*25)
        print("\t\t\t1. Update the items list\n\t\t\t2. Dispatch order\n\t\t\t3. View the item list\n\t\t\t4.Close\n")
        n1=int(input("enter according to the above menu: "))
        if n1==1:
            items.update() 
        elif n1==2:
            orders.dispatch()
        elif n1==3:
            fp=open("items.txt")
            print(fp.read())
            fp.close()
        elif n1==4:
            print("-"*25,"Thank you","-"*25)
            break