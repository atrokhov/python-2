import math
def function():
	print("Hello")

function()

def empty_function():
	pass

empty_function()

def add(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiply(a, b):
	return a * b

def division(a, b):
	return a / b

while True:
	a = int(input("First number: "))
	b = int(input("Second number: "))
	c = input("Operator: ")

	if c == "+":
		print(add(a, b))
	elif c == "-":
		print(subtraction(a, b))
	elif c == "*":
		print(multiply(a, b))
	elif c == "/":
		print(division(a, b))
	else:
		print("Wrong input")