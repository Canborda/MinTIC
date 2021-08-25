import random as rd
import time 

end=9
start=1
hide="*"
seconds=1
score=0
round=0

tecl=input("Press Enter to start")

print("\n¡WELCOME TO THE MEMORY GAME!\n")

while True:
    aleat=rd.randint(start, end)
    print("Memorize: ", aleat, end="\r")
    time.sleep(seconds)
    print("Memorize: ", hide)
    num=int(input("Your turn: "))

    if num==aleat:
        end=end*10
        start=start*10
        hide=hide+"*"
        seconds=seconds+0.2
        round=round+1
        score=score+round
        print("¡CORRECT!")
        print("Your score is: ", score, "\n")

    else:
        print("\n¡INCORRECT! :'(\n")
        for i,j in zip (str(aleat), str(num)):
            if i==j:
                score=score+1
            else:
                score=score+0
        print("Your score is: ", score, "\n")
        break       
    


        
        


    


        

