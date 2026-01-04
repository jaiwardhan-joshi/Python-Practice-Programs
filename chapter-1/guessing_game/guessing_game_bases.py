import random

def guess_game() :
    
     genNumber = random.randint(0,100)
     base_number = random.randint(2,16)
     print(f"Guess the number (0 to 100 in decimal), but enter it in base {base_number}")
     i = 0
     while True :
        try :
            userNumber = int(input(f"Enter your number in {base_number} :"), base_number)
            i = i + 1
            if userNumber > genNumber :
                print("Number is too high")

            elif userNumber < genNumber :
                print("Number is too low")
                

            elif userNumber == genNumber :
                print(f"You are right!")
                break    
            
            
        except ValueError :
            print("Invalid number for this base")

     print(f"Done in {i} chances.")
    
guess_game()



 