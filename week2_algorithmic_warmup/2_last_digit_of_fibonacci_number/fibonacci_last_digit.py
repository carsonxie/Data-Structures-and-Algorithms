# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def calc_fib_faster(n):
    Fib = [0,1]
    
    for i in range(2,n+1):
        #Fib[i] = Fib[i-1] + Fib[i-2]
        last_sum = Fib[i-1] + Fib[i-2]
        Fib.append(last_sum)

    current = Fib[n]
    return current % 10

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    n = int(input())
    print(calc_fib_faster(n))
