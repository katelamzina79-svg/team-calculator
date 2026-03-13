# utils.py - Математические функции
def add(a, b):
	return round(a+b, 2)
def subtract(a,b):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("Аргументы должны быть числами")
	return a-b
