pages = 100
lines = 50
symbols = 25

all_sym = pages * lines * symbols

one_sym = 4 * all_sym

disk = 1.44 * 1024 ** 2

count_books = disk // one_sym
count_books = round(count_books)

print("Количество книг, помещающихся на дискету:", count_books)


# TODO Найдите количество книг, которое можно разместить на дискете

