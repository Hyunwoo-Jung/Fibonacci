# n이 커지면 처리에 시간이 오래 걸려 처리 결과를 저장하는 방법
# 이러한 방법을 memoization

memo = {1: 1, 2: 1} # 사전(Dictionary)에 종료 조건 입력

def fibonacci(n):
    if n in memo:
        return memo[n] # 사전에 등록되어 있으면 그 값을 반환
    
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
    
    return memo[n]

print(fibonacci(8))    