import random
number=random.randint(1,100)
print("I'm thinking of a number between 1 and 100!")

attempts=5
guess=int(input("Enter your guess:"))
while guess !=number and attempts>0:
    attempts -=1
    if guess<number:
        print(f"Too low! {attempts} attempts left.")
    else:
        print(f"Too high! {attempts} attempts left.")
    if attempts>0:
        guess=int(input("Enter your guess:"))

if guess== number:
    print("Congratulations!You gussed it right!")
else:
    print(f"Game over! The number was {number}.")    


