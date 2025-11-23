#Simple project of Contact book using file i/o
#Add contacts, search contacts by name, and save to a file.

def save_contact(name,cno):     #it save the contact in file
    with open("contact.txt","a") as f:
        f.write(f"Contact name:{name}            Contact no.{cno}\n")
    print("**********************//Contact Saved!//************************")

def delete_contact(name,cno):       #it delete the contact from file
    with open("contact.txt") as f:
        lines=f.readlines()
    with open("contact.txt","w") as f:
        for line in lines:
            if name not in line and cno not in line:
                f.write(line)
        print("**********************//Contact Deleted//***********************")

def search_contact(name,cno):       #searching contact from file
    with open("contact.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            if name in line or cno in line:
                print(f"***************//{name}{cno} FOUND...//*******************")
                break
        else:
            print(f"****************//{name}{cno} IS NOT FOUND...!//**************")

def watch_contact():        #watch full file of contact
    with open("contact.txt") as f:
        list=f.read()
        print("**********************//CONTACT LIST//**************************")
        print(list)

loop=True
while loop:
    operation=int(input("****************************************************************"
    "\n1.Save Contact\n2.Delete Contact\n3.Search contact\n4.Watch Contact list\n5.EXIT!\n"
    "****************************************************************"
    "\nEnter your operation no.:\n"))
    if (operation==1):
        name=input("Enter the Contact name:")
        cno=input("Enter the Contact number:")
        save_contact(name,cno)
    elif(operation==2):
        name=input("Enter the Contact name:")
        cno=input("Enter the Contact number:")
        delete_contact(name,cno)
    elif(operation==3):
        print("YOU CAN ALSO SEARCH ONLY NAME!")
        name=input("Enter the Contact name:")
        cno=input("Enter the Contact number:")
        search_contact(name,cno)
    elif(operation==4):
        watch_contact()
    elif(operation==5):
        break
    else:
        print("//INVILED CHOICE//")
