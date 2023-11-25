import random

def play_guess_the_number():
    print("Вітаємо у грі 'Вгадай число'!")
    print("Я загадав число від 1 до 100. Спробуйте вгадати.")

    secret_number=random.randint(1,100)
    attempts=0

    while True:
        try:
            guess=int(input("Вгадаєте число?: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        attempts +=1

        if guess==secret_number:
            print(f"Ви вгадали! Число було {secret_number}. Вам знадобилося {attempts} спроб.")
            break
        elif guess<secret_number:
            print("Загадане число більше. Спробуйте ще.")
        else:
            print("Загадане число менше. Спробуйте ще.")

play_guess_the_number()
