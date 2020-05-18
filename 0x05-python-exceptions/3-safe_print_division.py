#!/usr/bin/python3
def safe_print_division(a, b):
	try:
		tmp = a / b
		return tmp
	except ZeroDivisionError:
		tmp = None
		print('Inside result: None')
		return tmp
	finally:
		if tmp:
			print('Inside result: {}'.format(tmp))
