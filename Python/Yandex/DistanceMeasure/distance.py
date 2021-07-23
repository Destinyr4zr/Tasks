import sys
import itertools


def distanceMeasure(arr, sublen):
    res = ""
    for i in range(1, len(arr) + 1):
        measures = []
        for subseq in itertools.combinations(arr[:i-1] + arr[i:], sublen):
            cache = 0
            for j in range(sublen):
                cache += abs(arr[i-1] - subseq[j])
            measures.append(cache)
        res += f"{str(min(measures))} "
    print(res)


if __name__ == '__main__':
    readflag = 0
    for line in sys.stdin:
        if not readflag:
            _, sublen = line.split()
            readflag = 1
        else:
            arr = list(map(int, line.split()))
    distanceMeasure(arr, int(sublen))
