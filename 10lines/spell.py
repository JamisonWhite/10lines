from os import system

name = raw_input("Spell what? ")
system("say " + name)
for i in range(0,len(name)):
	print name[i]
	if name[i].isalnum():
		system("say  " + name[i])
	else:
		system("say bubbles")
