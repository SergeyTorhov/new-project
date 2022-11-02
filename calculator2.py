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
	print("111111111111")
	print("2222222222")	
	print("333333333")	
	print("4444444444444444")		
