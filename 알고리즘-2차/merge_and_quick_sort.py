import random
import time


def main():

    ###################
    #   Create List   #
    ###################

    n = 1000
    s = []

    for i in range(n):
        s.append(random.randint(0, n))  # s의 크기를 n만큼 설정한다.

    s1 = s.copy()                       # s의 내용을 각각 s1과
    s2 = s.copy()                       # s2에 복사하고
    s.sort()                            # 리스트 s를 정렬한다

    # Merge Sort와 Quick Sort의 결과를 출력해서 확인하는 문장
    # print("s1:", s1)  # merge sort
    # print("s2:", s2)  # quick sort
    # print()

    #
    #  Merge Sort와 Quick Sort의 실행시간을 비교한다.
    #
    ##################
    #   Merge Sort   #
    ##################
    # 랜덤 리스트 s1의 s[0,len(s1)-1]의 원소들 병합 정렬을 이용하여 정렬
    # 아무 의미없이 분할하고 후에 합병하여 정렬한다(정복)
    start = time.perf_counter()
    merge_sort(s=s1, low=0, high=len(s1) - 1)
    end = time.perf_counter()
    print("[Merge Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
 #   print("s1:", s1)
    print("Correct:", s == s1)
    print()

    ##################
    #   Quick Sort   #
    ##################
    # 랜덤 리스트 s2의 [0,len(s2)-1]의 원소들을 퀵 정렬을 이용하여 정렬
    # 분할과 동시에 정렬(정복)이 진행된다.
    start = time.perf_counter()
    quick_sort(s=s2, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Quick Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
  #  print("s2:", s2)
    print("Correct:", s == s2)
    print()

    #############
    #   TRIAL   #
    #############

    TRIAL = 100
    total_elapsed_time_merge_sort = 0
    total_elapsed_time_quick_sort = 0
    #
    print("[progressing] - TRIAL: {}".format(TRIAL))
    print(">" * (TRIAL // (TRIAL // 20)))

    for trial in range(TRIAL):
        # Create list
        n = 1000
        s = []
        for i in range(n):
            s.append(random.randint(0, n))

        s1 = s.copy()
        s2 = s.copy()

        # Merge Sort
        start = time.perf_counter()
        merge_sort(s=s1, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_merge_sort += end - start

        # Merge Sort
        start = time.perf_counter()
        quick_sort(s=s2, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_quick_sort += end - start

        if TRIAL >= 20 and (trial + 1) % (TRIAL // 20) == 0:
            print(">", end="", flush=True)

    print()
    print("Merge Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort))
    print("Quick Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort))


def merge_sort(s, low, high):           # 분할과 정복으로 구현된 병합 정렬 함수
    if low < high:
        mid = (low + high) // 2         # low와 high의 중간 지점 계산 ==> 내림 연산 : ⌊(low + high) / 2⌋
        merge_sort(s, low, mid)         # 분할① : 전반부(low ~ mid까지) 정렬
        merge_sort(s, mid + 1, high)    # 분할② : 후반부(mid + 1 ~ high까지) 정렬
        merge(s, low, mid, high)        # 정복(병합_Merge) : 분할①과 분할②를 합친다.



def merge(s, low, mid, high):
    tmp = [0] * (high - low + 1)    #high ~ low의 크기를 갖는 임시 리스트 tmp
    # i는 0 ~ mid, j는 mid ~ high를 이동하고
    # s[i]와 s[j]가 릴레이 가위바위보를 하듯이 비교를 진행하며
    # 둘 중 작은 값이 tmp[t]에 저장되고 인덱스가 이동된다
    i = low
    j = mid + 1
    t = 0
    while (i <= mid) & (j <= high):
        if s[i] <= s[j]:
            tmp[t] = s[i]
            t += 1
            i += 1
        else:
            tmp[t] = s[j]
            t += 1
            j += 1
    # 비교 후에 남은 것은 tmp에 남은 부분에 순차적으로 저장된다
    while i <= mid:
        tmp[t] = s[i]
        t += 1
        i += 1
    while j <= high:
        tmp[t] = s[j]
        t += 1
        j += 1
    i = low
    t = 0
    # 정렬이 끝난 tmp를 s에 순차적으로 넣으며 마무리한다
    while i <= high:
        s[i] = tmp[t]
        i += 1
        t += 1


def quick_sort(s, low, high):                   # 분할과 정복을 이용한 퀵 정렬 함수
    if low < high:
        pivot = partition(s, low, high)         # 분할 : partition의 결과값을 pivot에 대입
        quick_sort(s, low, pivot - 1)           # 좌측(low ~ pivot - 1) 리스트 정렬
        quick_sort(s, pivot + 1, high)          # 우측(pivot + 1 ~ high) 리스트 정렬



def partition(s, low, high):
    # partition은 일정한 기록을 갖는 사람들의 릴레이 뜀틀 과정이라 생각할 수 있다.
    # ①뜀틀의 기준을 줄에서 가장 뒤에 서 있는 사람의 기록(pivot)이라 가정하고
    # ②피봇을 제외하고 뜀틀을 넘은 사람과 뜀틀을 넘지 못한 사람으로 나누어
    # ③넘은 사람중 첫 사람과 넘지 못한 사람의 자리를 바꿔주는 방식으로
    # ④줄을 세운 뒤 pivot과 넘은 사람중 첫 사람 자리를 바꿔주고 ①의 과정을 반복한다.
    # 조건 : 사람들의 기록은 항상 일정하고 서로 다른 수치를 갖는다.
    # 위의 과정을 계속하면 결국 분할되면서 함께 자리도 정렬되는 효과를 얻을 수 있다.
    x = s[high]                        	# 기준 원소 x (pivot) : 맨 끝 원소
    i = low - 1                        	# i는 가장 처음(왼쪽) 지점
    for j in range(low, high):             	# j는 오른쪽으로 이동하며 x와 s[j] 비교
        if s[j] <= x:			# 뜀틀을 못 넘었다면
            i += 1			# j라는 사람은 i + 1에 자리한다.
            s[i], s[j] = s[j], s[i]
    i += 1				# 마지막에 끝자리의 피벗을
    j += 1				# 뜀틀을 못 넘은 사람 뒤에 넣고
    s[i], s[j] = s[j], s[i]			# 자리를 바꿔준다.
    return i				# 그리고 바뀐 피벗의 인덱스를 반환한다.


if __name__ == "__main__":
    main()
