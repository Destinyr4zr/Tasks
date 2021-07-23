from datetime import datetime, timedelta
from sys import stdin

if __name__ == '__main__':
    lines = stdin.readlines()
    resulttime = timedelta()
    for line in lines:
        points = line.split("-")
        resulttime += (datetime.strptime(points[1].strip(), "%S:%M:%H") - datetime.strptime(points[0].strip(), "%S:%M:%H"))
    print(resulttime.seconds)
