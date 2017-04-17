from contextlib import closing 

# If you have something (aka any class that can close)
# use a built in or make your own
class SomeCoolClass:
	def __init__(self):
		print "constructor on SomeCoolClass called"	
	def close(self):
		print "cool class close got called"


sc = SomeCoolClass()
with closing(sc):
	print "doing something"
	
	# close gets called no matter if you get an exception
	# raise ValueError("got an error")
