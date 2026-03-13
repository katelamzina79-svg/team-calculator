# utils.py - Математические функции
<<<<<<< HEAD
def add(a, b):
	return round(a+b, 2)
def subtract(a,b):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("Аргументы должны быть числами")
	return a-b
def multiply(a,b):
	return a*b
def divide:
	if b == 0:
		raise ValueError("На ноль делить нельзя")
	return a/b
