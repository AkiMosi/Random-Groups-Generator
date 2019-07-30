import numpy as np
import random as rnd

def genGroup():
    number_of_groups=5
    #number_of_groups=int(input("Enter the Number of groups : "))
    groups=[]
    names=["Aakash Babu","Ajay Damodar","Akileshvar A","Arun Kumar T",
           "Harini S","Janani","Jayaram","Joel Anthony Xavier","Kamalam",
           "Kausik R Ipour","Kavinila","Kaviya","Keerthana","Krishmitha",
           "Mahaboob Basha","Manoji Kumar","Meera","Midun Raju C","Monisha",
           "Mukund E","Nandhini C","Neha S","Nitha","Oviya","Prakash B",
           "Rashmi K","Sanjana","Shrinidhi","Shruthi R","Sreenila","Srinitha",
           "Sruthi B","Sruthi S","Surya N","Vigneshwaran S","Tarun Kumar M M",
           "Vikhram R A","Visalatchi"]
    total_strength=38
#    print("There will be a group with ", total_strength%number_of_groups,
#          'members\n Or there should be a equal spread ?(y/n) : ')
#    choice=input()
#    if(choice=='n'):
#        print("")
#    else:
#        print("")
    lst=list(np.arange(1,41,1))
    lst.remove(2)
    lst.remove(15)
    ds=dict(zip(lst,names))
    lst_copy=list(lst)
    members_per_group=int(total_strength/number_of_groups)
    for i in range(number_of_groups):
        temp=[]
        for j in range(members_per_group):
            temp.append(rnd.choice(lst_copy))
            lst_copy.remove(temp[j])
            temp[j]=ds[temp[j]]
        groups.append(temp)
        members_per_group=int(len(lst_copy)/(number_of_groups-i+1))
        print(len(lst_copy)," ",members_per_group)
    if(len(lst_copy)>0):
        temp=[]
        for i in range(len(lst_copy)):
            temp.append(rnd.choice(lst_copy))
            lst_copy.remove(temp[i])
            temp[i]=ds[temp[i]]
        groups.append(temp)
    del lst_copy
    return groups

def printGroup(groups):
    for i in range(len(groups)):
        print("Group ",i+1,' : ')
        for j in range(len(groups[i])):
            print(j+1,". ",groups[i][j])
            
def main():
    flag=0
    print("Hello, World")
    while(True):
        print("\n\n\nEnter the choice : \n1. Generate Groups \n2. Print the Ge"
              "nerated Group\n3. Exit")
        choice=int(input())
        if(choice==1):
            groups=genGroup()
            flag=1
            print("Groups Generated")
        elif(choice==2):
            if(flag==0):
                print("Generate the group first!")
            printGroup(groups)
        elif(choice==3):
            print("Thank You, Have a Great Day ")
            return

main()
