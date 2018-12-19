from collections import deque


def main():
    SET = int(input())
    for _ in range(SET):
        l = input().split()
        N = int(l[0])
        S = int(l[1])
        Q = int(l[2])
        platform = []
        sumLen = 0
        for i in range(N):
            temp = input().split()
            sumLen += int(temp[0])
            platform.append(deque([int(i) - 1 for i in temp[1:]]))

        car = []
        pos = 0
        time = 0

        while True:
            while len(car) > 0:
                if car[-1] == pos:
                    car.pop()
                    sumLen -= 1
                elif len(platform[pos]) < Q:
                    platform[pos].append(car[-1])
                    car.pop()
                else:
                    break
                time += 1
            while len(platform[pos]) > 0 and len(car) < S:
                car.append(platform[pos].popleft())
                time += 1
            pos += 1
            if pos == N:
                pos = 0
            if sumLen == 0:
                print(time)
                break
            time += 2


main()