from kmp import kmp_search
from boyermoore import boyer_moore_search
from rabinkarp import rabin_karp_search
import timeit

algorithms = {
    "Кнута-Морріса-Пратта": kmp_search,
    "Боєра-Мура": boyer_moore_search,
    "Рабіна-Карпа": rabin_karp_search,
}

texts_existing = [
    "бінарний пошук",
    "структури даних",
    "хеш-таблиця"
]

texts_non_existing = [
    "бінарнийabcdexyz",
    "структуриabcdexyz",
    "хешabcdexyz",
]

file = open("article1.txt", "r", encoding="utf-8")
article1 = file.read()
file.close()
file = open("article2.txt", "r", encoding="utf-8")
article2 = file.read()
file.close()

print("\nПошук існуючих фраз в обої статтях:")
for phrase in texts_existing:
    for alg_name, func in algorithms.items():
        result_article1 = timeit.timeit(lambda: func(article1, phrase), number=10)
        result_article2 = timeit.timeit(lambda: func(article2, phrase), number=10)
        print(f"Пошук {alg_name} фрази '{phrase}' в статті 1: Середній час = {result_article1:.6f} сек")
        print(f"Пошук {alg_name} фрази '{phrase}' в статті 2: Середній час = {result_article2:.6f} сек")
    print("")

print("\nПошук неіснуючих фраз в обої статтях:")
for phrase in texts_non_existing:
    for alg_name, func in algorithms.items():
        result_article1 = timeit.timeit(lambda: func(article1, phrase), number=10)
        result_article2 = timeit.timeit(lambda: func(article2, phrase), number=10)
        print(f"Пошук {alg_name} неіснуючої фрази '{phrase}' в статті 1: Середній час = {result_article1:.6f} сек")
        print(f"Пошук {alg_name} неіснуючої фрази '{phrase}' в статті 2: Середній час = {result_article2:.6f} сек")
    print("")