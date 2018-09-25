from Cards import *
import random

def printCard(n):
	print ("-----------------------------")
	print ("| "+cards[n])
	print ("-----------------------------")	
	print ("    "+cards[n])

printCard(random.randint(1, 22))
