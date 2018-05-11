def just_do_it(text):
	"Capitalize all words in <text>"
	from string import capwords
	return capwords(text)


if __name__ == '__main__':
	import doctest
	doctest.testmod()