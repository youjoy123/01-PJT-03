# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

# -1으로 역순 설정을 해줘야하며, 반대로 프린트해주는 조건값을 설정해야할 것.
# 문자를 하나씩 쪼갤 수 있도록 list 이용해야 할 것

t = int(input())

for tc in range(1, t + 1) :
    data = input()
    result = ""

    for i in range(len(data) - 1, -1, -1) :
        if data[i] == 'b' :
            result += 'd'
        elif data[i] == 'd' :
            result += 'b'
        elif data[i] == 'p' :
            result += 'q'
        else :
            result += 'p'

    print('#%d %s' % (tc, result))