import sys
import re


def ipCheck(string):
    if re.search("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", string):
        return string
    else:
        return None


def operationLogCount():
    ipbase = {}
    for line in sys.stdin:
        if (len(line.strip())>1 and line.find(']') != -1):
            _, log = line.split(']')
            log=log.strip().split()
            for part in log:
                part.strip()
                if ipCheck(part)!=None:
                    if part in ipbase:
                        ipbase[part] += 1
                    else:
                        ipbase[part] = 1
    for item in sorted(ipbase.items(), key=lambda item: item[1], reverse=True):
        print(f"{item[0]} {item[1]}")



if __name__ == '__main__':
    operationLogCount()
