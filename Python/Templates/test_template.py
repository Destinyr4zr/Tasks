from contextlib import redirect_stdout


def file_input(path):
    res = []
    with open(path, 'r') as infile:
        for line in infile:
            res.append(line)
    return res


def output_check(outpath, testpath):
    out_arr = file_input(outpath)
    test_arr = file_input(testpath)
    errors = {}
    for i in range(min(len(out_arr), len(test_arr))):
        if out_arr[i] != test_arr[i]:
            for j in range(min(len(out_arr[i]), len(test_arr[i]))):
                if out_arr[i][j] != test_arr[i][j]:
                    if f"Строка {i + 1}" not in errors:
                        errors[f"Строка {i + 1}"] = [f"{j}"]
                    else:
                        errors[f"Строка {i + 1}"].append(f"{j}")
    if len(errors) > 0:
        print(testpath, " Ошибки:")
        print(errors)
        for err in errors:
            print(err)
            print(errors[err])
        print("\n\n")
    else:
        print(testpath, " Ошибок нет\n\n")


def test_code_exec(inpath, outpath):
    with open(outpath, 'w+') as outfile, open(inpath, 'r') as infile:
        with redirect_stdout(outfile):
            file_contents = infile.read()
            exec(file_contents)
    return outpath


def test(func, checkfunc, inputfunc=None, outputfunc=None):
    TEST_NUMS = list(range(1,12))
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "output.txt"
    TEST_FILE = "test.txt"
    for i in TEST_NUMS:
        CURRENT_TEST = "./tests/" + str(i) + "/"
        if not inputfunc:
            if outputfunc:
                checkfunc(outputfunc(func(CURRENT_TEST + INPUT_FILE, CURRENT_TEST + OUTPUT_FILE)))
            else:
                checkfunc(func(CURRENT_TEST + INPUT_FILE, CURRENT_TEST + OUTPUT_FILE), CURRENT_TEST + TEST_FILE)
        else:
            checkfunc(outputfunc(func(inputfunc(CURRENT_TEST + INPUT_FILE)), CURRENT_TEST + OUTPUT_FILE),
                      CURRENT_TEST + TEST_FILE)


# def prod(func, inputfunc=None, outputfunc=None):
#     outputfunc(func(inputfunc()))


if __name__ == "__main__":
    test(test_code_exec, output_check)
