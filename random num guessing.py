import random  

print("hii! Welcome to the number guessing game.\nyou have 7 chances to guess the num.let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"You have 7 chances to the number between {low} nad {high}. Let's Start!")

num = random.randint(low,high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    
    if guess == num:
        print(f'Correct! the number is {num}. You guessed it {gc} attempts')
        break
    
    elif gc >= ch and gc != num:
        print(f'Orry! The number was {num}. Better luck next time.')
        
    elif guess > num:
        print('Too High! Try a lower number.')
        
    elif guess < num:
        print("Too Low! Try a higher number.")