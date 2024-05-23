import random                               # 수를 무작위로 뽑기 위해 사용된 라이브러리
import time                                 # 수행 시간 분석을 위해 사용된 라이브러리
import sys                                  # 재귀의 최대 깊이를 변경하기 위한 라이브러리
sys.setrecursionlimit(10**8)                # 최대 깊이를 998에서 100000000으로 변경

def main():
    num = 1_000_0000                        # num == 아이템의 개수
    s = []                                  # s == 아이템을 담는 리스트

    for value in range(num):                # 무작위로 num개의 수를 s리스트에 넣는 반복문
        s.append(random.randint(0, num))

    #key = s[random.randint(0, num)]            # key == 검색 대상이 되는 num 이하의 자연수
    key = random.randint(0, num)
    border_1 = 0                         # border_1 == 부분리스트 1, 2의 경계
    border_2 = num-1                 # border_2 == 부분리스트 2, 3의 경계
    s.sort()                                #삼진검색을 위한 리스트 정렬
    # 1. 삼진검색_Ternary Search Result 실행

    # 수행 전후의 시간을 start, end로 비교
    start = time.perf_counter()
    location = ternary_search(s, key, border_1, border_2)
    end = time.perf_counter()

    #print(s)
    print("[Ternary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start)*1000))
    print()


# 1. 삼진검색 함수 본문
def ternary_search(s, key, low, high):
    #과정 1. 초기화
    num = len(s)                            # num == s의 길이
    mid1 = low + (high - low) // 3          # mid1 == 부분리스트 1, 2의 경계
    mid2 = high - (high - low) // 3         # mid2 == 부분리스트 2, 3의 경계
    if s[mid1] == key:                      # mid1이 키일 때
        return mid1
    elif s[mid2] == key:                    # mid2이 키일 때
        return mid2
    elif key < s[mid1]:                     # (low, mid1)일 떄
        return ternary_search(s, key, low, mid1)
    elif key < s[mid2]:                     # (mid1, mid2)일 때
        return ternary_search(s, key, mid1+1, mid2)
    elif key < high:                        # (mid2, high)일 때
        return ternary_search(s, key, mid2+1, high)
    else:
        return -1

if __name__ == "__main__":
    main()
