print("Hesap makinesine hoşgeldiniz.")

while True:

	number_1 = float(input("İlk sayıyı seçiniz: "))

	number_2 = float(input("İkinci sayıyı seçiniz: "))

	process = input("+,-,*,/ işlemlerinden birini seçiniz: ")


	if process == "+":
		result = number_1 + number_2
		print(result)

	elif process == "-":
		result = number_1 - number_2
		print(result)

	elif process == "*":
		result = number_1 * number_2
		print(result)

	elif process == "/":		
		result = number_1 / number_2 
		print(result)

	else:
		print("Hatalı işlem bilgisi.")
