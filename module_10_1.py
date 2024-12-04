import threading
from time import *

def write_words(word_count, file_name):
    with open(file_name, "a",   encoding = "utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово №{i + 1}")
            file.write("\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    return " "

r = time()
print(write_words(10, "example1.txt"))
print(write_words(30, "example2.txt"))
print(write_words(200, "example3.txt"))
print(write_words(100, "example4.txt"))
t = time()
tr = t - r
print(f"Класическое выполнение програмы заняло {int(tr)} \n")

ex5 = threading.Thread(target=write_words, args=(10, "example5.txt"))
ex6 = threading.Thread(target=write_words, args= (30, "example6.txt"))
ex7 = threading.Thread(target=write_words, args= (200, "example7.txt"))
ex8 = threading.Thread(target=write_words, args= (100, "example8.txt"))


a = time()
ex5.start()
ex6.start()
ex7.start()
ex8.start()

ex5.join()
ex6.join()
ex7.join()
ex8.join()

b = time()
c = b - a
print(f"Многопотосность справвилась с задачей за {int(c)} секунд")
