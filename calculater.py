def add(x,y):
    print(f"The Sum of The Numbers is {x+y}")
def sub(x,y):
    print(f"The Subtraction of The Numbers is {x-y}")
def multi(x,y):
    print(f"The Multiplication of The Numbers is {x*y}")
def devide(x,y):
    print(f"The Devision of The Numbers is {x/y}")
def rem(x,y):
    print(f"The Remainder from Devison of The Numbers is {x%y}")

try:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome For Doing Some Calculations")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    while True:
        x=int(input("Enter First Number:"))
        y=int(input("Enter Second Number:"))
        print("--------------------------")
        print(" Enter 1 -> For Addition \n Enter 2 -> For Subtraction \n Enter 3 -> For Multiplication \n Enter 4 -> For Devision \n Enter 5 -> For Finding Remainder" )
        print("--------------------------")

        a=int(input("Enter Your Choice :"))
        print("-")
        

        if a==1:
            add(x,y)
        elif a==2:
            sub(x,y)
        elif a==3:
            multi(x,y)
        elif a==4:
            devide(x,y)
        elif a==5:
            rem(x,y)
        else:
            print("Invalid Entry !")
        
        
        print("--------------------------")

        c=int(input("Enter 1 For Using Again\nEnter 0 For Exit\nEnter:"))
        if c==0:
            print("You Exit.")
            print("Thanks For Using.")
            break



        

except:
    print("Error : Somethint Went Wrong !")




