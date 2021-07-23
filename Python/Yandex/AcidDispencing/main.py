import sys


def acidDispencing(arr):
    if sum([arr[i + 1] - arr[i] >= 0 for i in range(len(arr) - 1)]) == len(arr) - 1:
        return arr[len(arr)-1]-arr[0]
    else:
        return -1


if __name__ == '__main__':
    readflag = 0
    for line in sys.stdin:
        if readflag:
            inparr = list(map(int, line.split()))
            print(acidDispencing(inparr))
        else:
            readflag = 1
