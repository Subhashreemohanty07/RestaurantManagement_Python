import items
fp=open("costumer.txt",)
details=fp.read()
fp.close()
def login():
    print("\t\t\t\t\t\t-----Costumer Page-----")
    print("\t1. Sign up\n\t2. Sign in")
    ch=int(input("enter 1 if you are a new user or 2 if you are an existing user: "))   
    if ch==1:
        while True:
            name=input("Enter your name: ")
            if name in details:
                print("try another user name!!,this name is already in our database")
                continue
            else:
                break
        
        while True:
            psr=input("Enter your password: ")
            spe=["@","#","$","%","!","/","?"]
            if len(psr)<6:
                print("at least 6 characters required")
                continue
            elif not any (char.isdigit() for char in psr):
                print("at least one digit")
                continue
            elif not any (char.isupper() for char in psr):
                print("at least one capital character")
                continue
            elif not any(char.islower() for char in psr):
                print("at least one small character")
                continue
            elif not any(char in spe for char in psr):
                print("at least one special character")
                continue
            else:
                print("Login successful")
                break
        fp=open("costumer.txt","a")
        content=name+","+psr+"\n"
        fp.write(content)
        fp.close()
        items.itemslist()
    elif ch==2:
        flag=0
        name=input("enter your name: ")
        fp=open("costumer.txt")
        content=fp.readlines()
        fp.close()
        for i in content:
            i=i.rstrip().split(",")
            if name ==i[0]:
                flag=1
                pswd=input("enter your password: ")
                if i[1]==pswd:
                    print("logged in successfully")
                    items.itemslist()
                    break
                else:
                    print("password is invalid")
                    break
                
        if flag==0:
            print("your name is not in our data!!")
            print("please try again")
                 
    else:
        print("invalid option")  
    print("="*150)

        
                
                
            
        