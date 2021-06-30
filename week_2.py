
def exercise_1():
    print('ejercicio 1')

    print("Exercise of Jonnathan")


def exercise_2():
    print('ejercicio 2')
    print('Exercise of Danielito')
    
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