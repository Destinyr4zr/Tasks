import sys


def jsonParse():
    for line in sys.stdin:
        line = line.replace("null", 'None')
        result = ""
        try:
            jsonarray = eval(line)
            for item in jsonarray.items():
                result += str({f"{item[0]}.{index}": value for index, value in enumerate(item[1])}).strip("{}") if type(item[1]) is list else ""
                result += str({f"{item[0]}.{key}": value for key, value in item[1].items()}).strip("{}") if type(item[1]) is dict else ""
                result += ", "
            return print("{", result[0:len(result) - 2], "}", sep="")
        except:
            return print({})


if __name__ == '__main__':
    jsonParse()
