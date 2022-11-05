def additionN(n):
	summ = 0
	strN = ""
	for i in range(n):
		if i != (n - 1):
			a = int(input("Введите операнд: "))
			strN += str(a)+" + "
			summ += a
		else:
			a = int(input("Введите операнд: "))
			summ += a
			strN += str(a)+" = " + str(summ)
			print(strN)
			print("Что еще?")	
		
typeOper = input("Выберите операцию: ")
countOper = int(input("Сколько операндов? "))

if typeOper == "+":
	additionN(countOper)
else:
	print("Операция не распознана!")
	print("Что-то еще?")