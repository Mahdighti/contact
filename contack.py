import os 
PACH = 'C:/Users/ARTOR-LAPTOP/Desktop/New folder/contacks/contack.txt' 
ch=1 
def Add_contact(name,number):
    f=open(PACH , 'r') 
    f.close() 
    f=open(PACH , 'a')  
    user_dict = f"{name} = {number}\n" 
    f.write(user_dict) 
    f.close() 
def search(name):
    found = False
    f=open(PACH,'r') 
    for line in f: 
        if name.lower() in line.lower():
            print("contact found",line.strip())
            found = True 
            break 
        if not found:
            print("contact not found") 
def view_all():
    f=open(PACH,'r')  
    data = f.readlines() 
    f.close() 
    print(data)  
while ch != 0 : 
    print("1.Add contact\n2.Search contact\n3.View contact\n0.exit") 
    choice = int(input("Enter your choice : ")) 
    if(choice == 1):
        name = input("enter your name : ")  
        number = str(input("enter your number : "))  
        Add_contact(name,number) 
    elif(choice == 2): 
        name = input("enter a name") 
        search(name) 
    elif(choice==3):
        view_all() 


     