__author__ = 'mwas'


def handle_exception(print_statement):
	def inner_handle_exception(func):
		def inner(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except Exception as ex:
				if print_statement:
					print ex.message
				return "n/a"
		return inner
	return inner_handle_exception


@handle_exception(False)
def divide(x, y):
	return x/y


print divide(8, 0)


