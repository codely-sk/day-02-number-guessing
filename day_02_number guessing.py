import random
secret_num = random.randint(1,100)
attempts=0
print ("Welcome to the number guessing game")
print ("I have choosen a number between 1 to 100. GUESS IT!")
while True:
    try:
        guess=int(input("enter yyour guess"))
    except ValueError:
        print ("Invalid input! enter a whole no.")
        continue

    attempts +=1

    if guess<1 or guess>100:
        print ("Please a no. between 1 to 100")
        continue
    if guess<secret_num:
        print("TOO LOW! try again")
    elif guess>secret_num:
        print("TOO HIGH! try again")
    else:
        print (f'CORRECT GUESS! you guessed it right in {attempts} attempts.')