import sys


def algoCheck():
    # for line in sys.stdin:
    line = input('\n')
    if len(line) > 1:
        arr = list(map(int, line.split()))
        # if(sum(arr)==arr[0]*2 and len(arr[1:])==arr[0]*2):
        if arr[-1] == 0:
            i = -2
            while i >= -len(arr):
                if arr[i] > 0 and sum(arr[i + arr[i]:i:-1]) == arr[i] - 1:
                    temp = arr[i]
                    try:
                        del arr[i + arr[i]:i:-1]
                    except:
                        return print(0)
                    i += temp
                i -= 1
            if len(arr) == 1:
                return print(1)
            else:
                return print(0)
        else:
            return print(0)
    else:
        return print(0)


if __name__ == '__main__':
    algoCheck()
