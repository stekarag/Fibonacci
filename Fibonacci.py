from functools import lru_cache
import sys
import time

@lru_cache(maxsize=None)
def fib(z):
	if z == 0:
		return 0
	elif z == 1:
		return 1
	else:
		prev = fib(z-1)
		prevv = fib(z-2)
		ret = prev + prevv
		return ret

def san(z):
	try:
		n = int(z)
	except ValueError:
		print("Input can only be a natural number.")
		exit()
	if n < 0:
		print("There are no negative Fibonacci numbers")
		exit()
	elif n < lim:
		an = fib(n)
		return an
	else: 
		print("Calculation of term %d and beyond is not possible"%lim)
		exit()


lim = int((sys.getrecursionlimit()/2)-1)
y = input("Which Fibonacci number do you want? ")
start = time.time()
ans = san(y)
if ans < 1000:
	print("The answer is %d"%ans)
else:
	print("The answer is %d, which is about %.2e"%(ans, ans))
end = time.time()
t = float((end - start)*1000000)
print("Calculating took %.3f microsecond(s)"%t)
