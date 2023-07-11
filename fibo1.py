def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1 # 처음 두 항은 1
    return fibonacci(n - 2) + fibonacci(n - 1) # 직전 두 항의 합
 
print(fibonacci(6)) # 피보나치수열의 6번째 항 출력