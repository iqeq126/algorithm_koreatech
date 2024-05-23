import random                               # 수를 무작위로 뽑기 위해 사용된 라이브러리
import time                                 # 수행 시간 분석을 위해 사용된 라이브러리

def main():
    # [주의 및 수행 사항 3, 4번 : num 변수를 1_000, 10_000, 100_000, 1_000_000으로 키우며 수행 시간을 비교]
    num = 1_00000                             # 수행 횟수 == num
    s = []                                  # s == 수행 대상이 되는 리스트 [주의 및 수행 사항 1번 : 배열 인덱스는 0~num-1까지 유효]

    for value in range(num):                # 무작위로 num개의 수를 s리스트에 넣는 반복문
        s.append(random.randint(0, num))

    key = random.randint(0, num)            # key == 검색 대상이 되는 num 이하의 자연수

    # 1. 순차검색_Sequential Search Result 실행

    # 수행 전후의 시간을 start, end로 비교
    # [주의 및 수행 사항 5 : num에 대한 각 함수의 수행시간 그래프 작성하기]
    start = time.time()
    location = sequential_search(s, key)
    end = time.time()

    #print(s)
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start)*1000))
    print()


    s.sort()                                #이진검색을 위한 리스트 정렬
    # 2. 이진검색(반복_분할정복)_Binary Search Result 실행

    # 수행 전후의 시간을 start, end로 비교
    # [주의 및 수행 사항 5 : num에 대한 각 함수의 수행시간 그래프 작성하기]
    start = time.time()
    location = binary_search(s, key)
    end = time.time()

    #print(s)
    print("[Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start)*1000))
    print()
    #3. 이진검색(재귀_분할정복)_Recursive Binary Search Result 실행

    # 수행 전후의 시간을 start, end로 비교
    # [주의 및 수행 사항 5 : num에 대한 각 함수의 수행시간 그래프 작성하기]
    start = time.time()
    location = recursive_binary_search(s, key, 0, num - 1)
    end = time.time()

    #print(s)
    print("[Recursive Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start)*1000))
    print()

# 1. 순차검색 함수 본문
def sequential_search(s, key):
    #과정 1. 초기화
    num = len(s)                            # num = s의 길이
    location = 0                            # 초기 위치를 0으로 지정 (이진검색과 다르게 순차검색을 하기에 값을 -1로 설정하지 않음)
    i = 1                                   # i == 검색 위치

    #과정 2. 순차검색 반복문 실행
    for i in s:                             # 0부터 배열의 끝까지 key 값에 대한 순차검색 실행
        #과정 3-1. 순차검색 성공한 경우
        if key == s[i-1]:                     # key 값이 존재할 경우 위치(i)를 location에 대입 후 반복 탈출
            location = i-1
            break
    #과정 3-2. 순차검색 실패한 경우
    if location == 0:                       # [주의 및 수행 사항 2번 : location에 변화가 없다면 -1 리턴]
         location = -1

    #과정 4. 최종 결과 리턴
    return location

# 2. 이진검색(반복_분할정복) 함수 본문
def binary_search(s, key):
    #과정 1. 초기화
    num = len(s)                            # num = s의 길이
    low = 0
    high = num - 1
    location = -1                           # [주의 및 수행 사항 2번 : location에 변화가 없다면 -1 리턴]

    #과정 2. 이진검색 반복문 실행
    while True:

        #과정 3. 탈출조건 정의 ( low가 high보다 커질 때 )
        if low > high: break

        #과정 4. 검색범위 지정
        mid = round((high + low) / 2)
        #과정 4-1. 같을 때
        if key == s[mid]:
            location = mid
            break
        #과정 4-2. key가 더 클 때
        elif key > s[mid]:
            low = mid + 1
        #과정 4-3. key가 더 작을 때
        else:
            high = mid - 1
    #과정 5. 최종결과 리턴
    return location

# 3. 이진검색(재귀_분할정복) 함수 본문
def recursive_binary_search(s, key, low, high):
    #과정 1. 탈출조건 정의 ( low가 high보다 커질 때 )
    if(low > high): return -1
    # [주의 및 수행 사항 2번 : location에 변화가 없다면 -1 리턴]

    #과정 2. 검색범위 지정
    mid = round((low + high) / 2)
    #과정 2-1. 같을 때
    if key == s[mid]:
        return mid
    #과정 2-1. key가 더 클 때
    elif key > s[mid]:
        return recursive_binary_search(s, key, mid + 1, high)
    #과정 2-3. key가 더 작을 때
    else:
        return recursive_binary_search(s, key, low, mid - 1)

if __name__ == "__main__":
    main()
