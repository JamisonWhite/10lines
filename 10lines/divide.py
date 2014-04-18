from os import system

top = int(raw_input("Top number? "))
bottom = int(raw_input("Bottom number? "))
divided = top / bottom
answer = str(top) + ' divided by ' + \
			str(bottom) + ' is ' + \
			str(divided) + '.' 
print answer
system("say " + answer)
