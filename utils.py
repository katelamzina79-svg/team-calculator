# utils.py - Математические функции
def subtract(a,b):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("Аргументы должны быть числами")
	return a-b
