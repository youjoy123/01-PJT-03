t = int(input())

for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = 0
    if data.count(data[0]) == 3 :
        result = data[0]
    else :
        if data.count(max(data)) == 1 :
            result = max(data)
        else :
            result = min(data)

    print('#%d %d' % (tc, result))