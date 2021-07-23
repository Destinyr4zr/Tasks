import sys

seatrow = ('A', 'B', 'C', 'D', 'E', 'F')


def memPrint(mem):
    for i in range(len(mem)):
        row = mem[i][0] + mem[i][1]
        line = []
        for j in range(6):
            if not (row[j]):
                line += '.'
            elif row[j] == 'X':
                line += row[j]
                mem[i][j // 3][j % 3] = 1
            else:
                line += '#'
            if j == 2:
                line += '_'
        print(''.join(line))


def samoletPacking(mem, req):
    global seatrow
    result = ""
    count, side, anch = req.split()
    count = int(count)
    side = 0 if side == "left" else 1
    if anch == "aisle":
        lo, hi = (0, count) if side else (3 - count, 3)
    else:
        lo, hi = (3 - count, 3) if side else (0, count)
    for k in range(len(mem)):
        if sum(mem[k][side][lo:hi]) == 0:
            result += "Passengers can take seats:"
            for m in range(side * 3 + lo, side * 3 + hi):
                result += f" {k + 1}{seatrow[m]}"
                mem[k][side][m - side * 3] = 'X'
            print(result)
            return True
    return False


if __name__ == '__main__':
    # lines = sys.stdin.readlines()
    #
    lines = []
    with open("input.txt", 'r') as infile:
        for line in infile:
            lines.append(line)
    #
    mem = []
    memlen = int(lines[0])
    for i in range(1, memlen + 1):
        mem.append([[], []])
        for j in range(7):
            if j != 3:
                if lines[i][j] == '#':
                    mem[i - 1][j // 4].append(1)
                else:
                    mem[i - 1][j // 4].append(0)
    for req in lines[memlen + 2:]:
        if samoletPacking(mem, req):
            memPrint(mem)
        else:
            print('Cannot fulfill passengers requirements')
