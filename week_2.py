
def exercise_1():
    print('ejercicio 1')
    print("Exercise of Daniel es gay")
    
    canta=int(input("How many sheets does it require?: "))
    canth=int(input("Amount of leaves on the branches?: "))
    cantr=int(input("Number of tree branches?: "))
    branches=0
    tree=0
    while (True):
        if canth <= canta:
            canta = canta - canth
            branches += 1
        if branches == cantr:
            branches = branches - cantr
            tree += 1
        if canth > canta:
            break
    
    print("You need ",tree, " trees, ",branches, " branches and ", canta, " sheets.")

    



def exercise_2():
    print('ejercicio 2')
    print('Exercise of Jonnathan' "\n")

    k = float(input("Enter your capital value: "))
    i = float(input("Enter your daily interest rate: "))
    t = float(input("Enter your interest time: "))

    print("\n""SIMPLE INTEREST" "\n")
    vf1= k * i * t
    print("Your simple interest to pay is ", vf1, "pesos ")
    vt1 = k + vf1
    print("Your total value to pay is ", vt1, "pesos" "\n")

    print("COMPOUND INTEREST" "\n")
    vf2 = k *(1+i)**t
    print("Your compound interest to pay is ", vf2, "pesos ")
    vt2 = k + vf2
    print("Your total value to pay is ", vt2, "pesos ")

    #Me gustaria hacerlo con funciones pero no se me da jaja me tocar mirar como lo puedo hacer.
    
def exercise_3():
    print('ejercicio 3')

def exercise_4():
    print('ejercicio 4')

def exercise_5():
    print('ejercicio 5')

def exercise_6():
    print('ejercicio 6')

def exercise_7():
    print('ejercicio 7')

# Loop

while(True):
    option = input('Select excercise (e to exit): ')

    if(option=='e'): break
    elif(option=='1'): exercise_1()
    elif(option=='2'): exercise_2()
    elif(option=='3'): exercise_3()
    elif(option=='4'): exercise_4()
    elif(option=='5'): exercise_5()
    elif(option=='6'): exercise_6()
    elif(option=='7'): exercise_7()
    else: print('ERROR: {} is not a command.'.format(option))

print('Program finished.')