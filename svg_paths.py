

"""
example string

<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
<rect fill="#fff" height="512" rx="15%" width="512"/>
<path d="m256 152c-52-1-100 43-103 95a103 103 0 0 0 200 43 104 104 0 0 0 -97-138zm0 169c-40 2-74-40-65-79 7-40 54-65 91-48 36 14 52 63 31 95a66 66 0 0 1 -57 32zm131-171c1 20-27 31-41 16-14-14-3-41 17-40 13 0 24 11 24 24z"/>
<path d="m424 89c-25-27-64-35-100-33-54 0-109-1-164 1-43 2-85 31-98 73-10 32-5 66-6 98 0 42-1 84 1 126 3 46 37 87 81 98 30 7 62 3 92 4 42 0 83 1 124-1 44-3 85-33 96-76 9-32 5-64 6-97 0-41 1-83-1-125-2-25-13-50-31-68zm-3 250c1 35-23 70-57 77-28 5-56 2-83 3-40-1-80 1-120-1-32-2-61-26-66-58-4-28-1-57-2-86 1-38-1-76 1-114 2-32 26-60 58-65 29-4 59-1 88-2 38 0 76-1 113 1 33 2 62 29 66 62 3 30 1 61 2 92z"/>
</svg>
"""

def parse_path(ts):
	"""
	"""
	index = 0
	s = ""
	res = []
	while True:
		try:
			cc = ts[index]
		except IndexError:
			print "broke for index error"
			break
		if cc == "a" or cc == "A" or cc == "m" or cc == "M" or cc == "z" or cc =="c":
			if s!="":
				print "DBG: s",s
				res.append(int(s))
				s = ""
			res.append(cc)
			index = index + 1
			continue
		if cc == "-":
			if s!="":
				# if s has something in it push it
				# and clear s
				res.append(int(s))
				s = "-"
			else:
				s = s + cc
		if cc in ["0","1","2","3","4","5","6","7","8","9"]:
			s = s + cc
		if cc == " " or cc == "\n" or cc == "\r" or cc == "\t":
			if s!="":
				res.append(int(s))
				s = ""
			
		index = index + 1

	print "done with gathering", s
	res.append(int(s))
	return res 

def parse_multiple_numbers(ts):
	"""
		parse multiple numbers in a string
		3 3 -3-4
	"""
	index = 0
	s = ""
	res = []
	while True:
		try:
			cc = ts[index]
		except IndexError:
			print "broke for index error"
			break
		if cc == "-":
			if s!="":
				# if s has something in it push it
				# and clear s
				res.append(int(s))
				s = "-"
			else:
				s = s + cc
		if cc in ["0","1","2","3","4","5","6","7","8","9"]:
			s = s + cc
		if cc == " " or cc == "\n" or cc == "\r" or cc == "\t":
			if s!="":
				res.append(int(s))
				s = ""
			
		index = index + 1

	print "done with gathering", s
	res.append(int(s))
	return res 

def parse_single_number(ts):
	index = 0
	s = ""
	while True:
		try:
			cc = ts[index]
		except IndexError:
			print "broke for index error"
			break
		if cc == "-":
			s = s + cc
		if cc in ["0","1","2","3","4","5","6","7","8","9"]:
			s = s + cc
		if cc == " " or cc == "\n" or cc == "\r" or cc == "\t":
			index = index + 1
			continue

		index = index + 1

	print "done with gathering", s
	return int(s)

def test_multiple_numbers_1():
	res = parse_multiple_numbers("-10-20")
	assert res[0] == -10
	assert res[1] == -20

def test_multiple_numbers_2():
	res = parse_multiple_numbers("-1")
	assert res[0] == -1

def test_multiple_numbers_3():
	res = parse_multiple_numbers("-2 -3")
	assert res[0] == -2
	assert res[1] == -3

def test_multiple_numbers_4():
	res = parse_multiple_numbers("-100-1-2")
	assert res[0] == -100
	assert res[1] == -1
	assert res[2] == -2

def test_parse_single_number_1():
	res = parse_single_number("-10")
	assert res == -10

def test_parse_single_number_2():
	res = parse_single_number("-10 ")
	assert res == -10

def test_path1():
	s ="m256 152c-52-1-100 43-103 95a103 103 0 0 0 200 43 104 104 0 0 0 -97-138zm0 169c-40 2-74-40-65-79 7-40 54-65 91-48 36 14 52 63 31 95a66 66 0 0 1 -57 32zm131-171c1 20-27 31-41 16-14-14-3-41 17-40 13 0 24 11 24 24z"

	print s
	print "---------------"
	return parse_path(s)

print test_path1()

