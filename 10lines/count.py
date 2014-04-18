from os import system

number = int(raw_input("How many? "))
while number >= 0: 
	print number
	system("say " + str(number))
	number = number - 1
