import time                                 # 수행 시간 분석을 위해 사용된 라이브러리


def main():
    # [주의 및 수행 사항 1, 2번 : num 변수를 키우며 수행 시간을 비교하고 기다릴 수 있는 최대 num 값 할당하기]
    num =10                              # 수행 횟수 == num
    # 1. 피보나치(DP)_Iterative Fibonacci 실행

    # 수행 전후의 시간을 start, end로 비교
    # [주의 및 수행 사항 3 : num에 대한 각 함수의 수행시간 그래프 작성하기]
    start = time.time()
    result1 = iterative_fibonacci(num)
    end = time.time()

    print("[Iterative Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result1))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

    # 2. 피보나치(재귀)_Recursive Fibonacci 실행

    # 수행 전후의 시간을 start, end로 비교
    # [주의 및 수행 사항 3 : num에 대한 각 함수의 수행시간 그래프 작성하기]
    start = time.time()
    result2 = recursive_fibonacci(num)
    end = time.time()

    print("[Recursive Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result2))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

# 1. 피보나치(DP) 함수 본문
def iterative_fibonacci(num):
    #과정 1. 초기화 실행
    i = 2
    s = []
    s.append(1)
    s.append(1)
    #과정 2. DP를 이용한 피보나치 초기화 실행
    while i < num:
        s.append(s[i - 1] + s[i - 2])
        i += 1
    #과정 3. 결과값 리턴
    return s[num-1]

# 2. 피보나치(재귀) 함수 본문
def recursive_fibonacci(num):
    #과정 1. 탈출조건 정의
   if 0 <= num < 2: return num
    #과정 2. 피보나치(재귀) 실행
   return recursive_fibonacci(num-2) + recursive_fibonacci(num-1)


if __name__ == "__main__":
    main()
