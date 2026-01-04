import random

def guess_game() :
    
     genNumber = random.randint(0,100)
     print(f"Guess the number 0 to 100 in integer")
     i = 3
     while True :
        try :
            userNumber = int(input(f"Enter your number:"))
            i = i - 1
            if userNumber > genNumber :
                print("Number is too high")

            elif userNumber < genNumber :
                print("Number is too low")
                

            elif userNumber == genNumber :
                print(f"You are right!")
                break    

            if i == 0 :
                print("Your Chances are up!")
                break
            
            print(f"{i} Chances Left .")

        except ValueError :
            print("Invalid input")
    
    
guess_game()



 