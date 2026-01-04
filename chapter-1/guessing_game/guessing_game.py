import random

def guess_game() :
    
     genNumber = random.randint(0,100)
     print(f"Guess the number 0 to 100 in integer")
     i = 0
     while True :
        try :
            userNumber = int(input(f"Enter your number:"))
            i = i + 1
            if userNumber > genNumber :
                print("Number is too high")

            elif userNumber < genNumber :
                print("Number is too low")
                

            elif userNumber == genNumber :
                print(f"You are right!")
                break    
            
            
        except ValueError :
            print("Invalid input")

     print(f"Done in {i} chances.")
    
guess_game()



 