import user
import owner
print()
print("*"*50,"restaurant page","*"*50)
print("\t1. Costumer\n\t2. Owner\n")
ch=int(input("enter your choice 1 or 2: "))
if ch==1:
    user.login()
elif ch==2:
    pswr=input("enter your password: ")
    if pswr=="Own@123":
        print("="*20,"Logged in successfully","="*20)
        owner.staff()
    else:
        print("SORRY!! wrong password")
else:
    print("Sorry!! invalid choice")
