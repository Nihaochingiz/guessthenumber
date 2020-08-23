import random

attempts = 0

number = random.randint(1, 20)
print("Я думаю о числах между 1 и 20.")

while attempts < 6:
	guess = input ("Попробуй угадать")
	guess = int (guess)

	attempts +=1

	if guess > number:
		print("Много")

	if guess < number:
		print("Мало")

	if guess == number:
		break
		if guess == number:
			attempts = str(attempts)
			print(f"Молодец! Ты угадал мою цифру  {attempts} !")	

		if guess != number:
			number = str(number)
			print(f"Нет, цифра, которую я загадал была {number}")	

