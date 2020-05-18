#!/usr/bin/python3
def safe_print_division(a, b):
	try:
		tmp = a / b
	except ZeroDivisionError:
		tmp = None
		print('Inside result: None')
	finally:
		if tmp:
			print('Inside result: {}'.format(tmp))
		return tmp
