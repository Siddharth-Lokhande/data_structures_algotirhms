#dsa assignment no.1

size=int(input("Enter size of hashtable="))
n=int(input("Enter no. of entries="))
hash_table=[-1]*size


def display():
    print("-------------------Telephone database----------------\nno.   telephone no.")
    for i in range(size):
        if(hash_table[i]==-1):
            print(i,"             ")
        else:
            print(i,hash_table[i])


def linear_probing(telephone_no):
    for i in range(size):
        index=(telephone_no%size+i)%size
        if(hash_table[index]==-1):
            hash_table[index]=telephone_no
            print("Telephone no. inserted")
            break
        else:
            print("Entry cannot be inserted")


def quadratic_probing(telephone_no):

    for i in range(size):
        index=((telephone_no%size)+i*i)%size
        if(hash_table[index]==-1):
            hash_table[index]=telephone_no
            print("telephone no. inserted")
            break
        else:
            i+=1
    else:
        print("Entry cannot be inserted")

def search(telephone_no):
    count=1
    for i in range(size):
        index=(telephone_no%size + i)%size
        if(hash_table[index]==telephone_no):
            print("telephone no.-",telephone_no," found at",index)
            print("no. of comparisons=",count)
            break
        else:
            count+=1
    else:
        print("Entry not found")



ch=1
while(ch==1):
    ch1=int(input("Menu-\n1)linear insert\n2)quadratic insert\n3)display\n4)search\nEnter choice="))
    if(ch1==1):
        for i in range(n):
            tele_no=int(input("Enter telephone no="))
            linear_probing(tele_no)
    elif(ch1==2):
        for i in range(n):
            tele_no=int(input("Enter telephone no="))
            quadratic_probing(tele_no)
    elif(ch1==3):
        display()
    elif(ch1==4):
        tele_no=int(input("Enter telephone no. to search="))
        search(tele_no)
    else:
        print("Invalid choice")

        ch=int(input("Do you want to continue?[yes-1,No-0]\nEnter choice="))

print("Thank you")