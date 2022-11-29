import os

INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"

if __name__=="__main__":
    testpath = os.path.join(os.getcwd(),"tests")
    if not os.path.isdir(testpath):
        os.makedirs(testpath)
        for i in range(1,12):
            subtestpath=os.path.join(testpath,f"{i}")
            if not os.path.isdir(subtestpath):
                os.makedirs(subtestpath)
                with open(os.path.join(subtestpath,INPUT_FILE),'x'):
                    pass
                with open(os.path.join(subtestpath,TEST_FILE),'x'):
                    pass
        print("Структура тестов добавлена")
    else:
        print("Уже существует")