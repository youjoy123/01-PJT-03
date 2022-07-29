# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# [출력]
# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

T=int(input())

for _ in range(T) :
    tc = int(input())
    score = list(map(int, input().split()))
    data = [0] * 1001
# 테스트 케이스 마다 번호를 입력 받기 위해 1000개 점수를 입력받게 해 리스트로 구현
# 0~1001개 담겨 있는 data 리스트 정의 후 반복문을 통해 score 값을 하나씩 확인
# 그 값을 인덱스로 하여 data리스트의 해당 인덱스값 증가
    for i in score :
        data[i] += 1

    max_value = max(data)
    result = []
    for i in range(len(data)) :
        if data[i] == max_value :
            result.append(i)

    print('#%d %d' % (tc, max(result)))