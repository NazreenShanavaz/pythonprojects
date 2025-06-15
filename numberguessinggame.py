import random

def giveHint(number):
    if number%2==0:
        print('Hint:number is even')
    else:
        print('Hint:number is odd')

    if number>50:
        print("Hint:the number is greater than 50")
    else:
        print("Hint:the number is lesser than 50")


def numberGuessingGame():
    win=0
    loss=0
    while True:
        number=random.randint(1,100)
        attempt=0
        max_attempt=5

        print('Welcome to the number guessing game:')
        print('I\'m thinking of a number between 1 and 100')
        print('Try and guess it..GOOD LUCK😉')

        while attempt<max_attempt:
            try:
                guess=int(input('enter your guess'))
                attempt+=1
            except ValueError:
                print('enter valid number')
                continue

            if attempt==3:
                giveHint(number)

            if guess>number:
                print('OOPS too high')
            elif guess<number:
                print('HAHA too low')
            else:
                print(f'CORRECT!! you have guessed in {attempt} atempts')
                win+=1
                break

        if guess != number:
            print(f"😢 Sorry! You’ve used all {max_attempt} attempts. The number was {number}.")
            loss+=1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Bye 😄")
            print('Game summary:')
            print(f'win:{win}')
            print(f'loss:{loss}')
            break


numberGuessingGame()

