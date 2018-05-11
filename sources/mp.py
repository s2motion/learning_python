import multiprocessing
import os

def do_this(what):
	do_whoami(what)

def do_whoami(what):
	print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
	do_whoami("I'm the main program")
	for n in range(4):
		p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
		p.start()