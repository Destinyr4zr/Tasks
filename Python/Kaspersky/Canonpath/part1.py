import sys

def Canonpath():
    for line in sys.stdin:
        if line[0]!='/':
            line='/'+line
        line=line.replace('../', '').replace('//','/')
        if len(line)>1 and line[len(line)-1] == '/':
            line=line[0:len(line)-1]
        return print(line)


if __name__ == '__main__':
    Canonpath()
