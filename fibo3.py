# 리스트에 순서대로 추가하는 방법

def fibonacci(n):
    fib = [1, 1]

    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    
    return fib[n - 1]

print(fibonacci(10))