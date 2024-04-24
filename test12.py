import random
print("Welcome to the coin fliping game!")
choice = input("Enter your side (Head or tails):")
num = random.randint(1,2)
if num==1:
    results="Heads"
elif num==2:
    results="Tails"
elif choice==results:
    print("Good job! You won, the coin flipped",results)
else:
    print("You lost, The coin flipped",results)
print("Thanks for playing")