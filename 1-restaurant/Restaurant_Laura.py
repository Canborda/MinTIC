
queue=[]
while True:
    option=input("(1) Enter order\n(2) Quit order\n(3) Exit\n")
    if(option=="1"):
        print("\n\n        MENU")
        print("Protein")
        print("(1) Beef\n(2) Chicken\n(3) Pork Meat\n")
        print("Accompaniments")
        print("(1) Bean\n(2) Spaghet\n(3) Lentils\n")
        print("Salad")
        print("(1) Sweet salad\n(2) Mexican Salad\n(3) Parisian salad\n")
        print("Juice")
        print("(1) Strawberry\n(2) Mango\n(3) Pineapple\n")

        if (len(queue)<5):
            #TODO limitar opciones <4
            order=input("Select menu: ")
            if order in queue: 
                print("\nThe order is repeated\n")
            else:
                queue.append(order)
                print(queue)
        else:
            print("\nImpossible to add more orders\n")
    elif(option=="2"):
        if (len(queue)>0):
            queue.pop(0)
            print(queue)
        else:
            print("Any order pending")
    elif(option=="3"):
        break
    else:
        print("Invalid option")
