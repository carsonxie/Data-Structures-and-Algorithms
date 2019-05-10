# Uses python3
'''different method to get fib number

'''
#naive way
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_faster(n):
	Fib = [0,1]
	
	for i in range(2,n+1):
		#Fib[i] = Fib[i-1] + Fib[i-2]
		last_sum = Fib[i-1] + Fib[i-2]
		Fib.append(last_sum)
	return Fib[n]


if __name__ == '__main__':
	n = int(input())
	#print(calc_fib(n))
	print(calc_fib_faster(n))
