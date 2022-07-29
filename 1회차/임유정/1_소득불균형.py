# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.
# 첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다. 
# 이 정수들은 각각 1 이상 100,000 이하이다.

# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    sum_value = sum(data)
    avg_value = sum_value / n

    result = 0
    for p in data :
        if p <= avg_value :
            result += 1
    # data 리스트의 요소를 하나씩 확인하여 해당 수가 평균 값 이하일 경우에만 값 1 증가
    print('#%d %d' % (tc, result))