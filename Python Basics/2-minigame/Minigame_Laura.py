import random as rd
import time

options="1"
while options=="1":
    side = int(input("enter side \n"))
    token=[rd.randint(0,side-1),rd.randint(0,side-1)]
    goal=[rd.randint(0,side-1),rd.randint(0,side-1)]
    for i in range(side):
        for j in range(side):
            if [i,j]==token:
                print("O", end=" ")
            elif [i,j]==goal:
                print("M", end=" ")
            else:
                print("*", end=" ")
        print(" ")

    while True:
        if token[0]<goal[0]:
            token[0]=token[0]+1
        elif token[0]>goal[0]:
            token[0]=token[0]-1
        elif token[1]<goal[1]:
            token[1]=token[1]+1
        elif token[1]>goal[1]:
            token[1]=token[1]-1

        print("\n")
        for i in range(side):
            for j in range(side):
                if [i,j]==token:
                    print("O", end=" ")
                elif [i,j]==goal:
                    print("M", end=" ")
                else:
                    print("*", end=" ")
            print(" ")
            
        time.sleep(0.5)
        if token==goal:
            print("CONGRATULATIONS! You reached the goal\n")
            options=input("Select the option: \n(1) Play again \n(2) Exit program\n")
            break
print ("Thank you!\n")
    
            




        
    