print("""===================100%===================""")
print('''
================================================
							SHOURYA'S IQ TEST
================================================''')
name = input("enter your name: ")

if name == False:
	name = 'andha'
	
qone = 'what is the shortcut used to run a python script in PyCharm?'
print(qone)
a=input("enter your answer: ")
if a == 'shift + f10':
	print("huh, thats an easy one, even a 2yr old can answer it easily 😒")
	
else:
	print("ewww, you can't even answer this, no worries that's not your problem, it's because you dosen't know how to function life")
	
qtwo = 'which keyword is used to create a reusable block of code in python'
print(qtwo)
b=input("enter your answer: ")
if b == 'def()':
	print("hmmm, impressive! but only for a millisecond 🤡")
	
else:
	print("did you ever listened the name of python as programming language? leave that i'm even thinking that do u even know what is programming language? 🤡'")
	
qthree='Why do exit() and quit() work perfectly in the interactive REPL (terminal) but can randomly fail or raise NameError in a production script run via a cron job or a minimal environment? What module injects them?'
print(qthree)
c=input("enter your final answer: ")
if c == 'exit() and quit() are helper instances of the Quitter class injected into the global namespace only by the site module':
	print("hmm, good, you broke my ego")
	exit()
	
else:
	print("FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!")
