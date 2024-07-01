n=10

a=0
b=1

fib_list=[]

for i in range(n):
    fib_list.append(a)
    a,b=b,a+b

print('The Fibonacci series are',fib_list)