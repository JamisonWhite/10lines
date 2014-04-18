from os import system

name = raw_input("Who are you? ")
for i in range(0,5):
	print name
	system("say " + name)