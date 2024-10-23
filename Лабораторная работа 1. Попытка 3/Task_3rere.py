# TODO Найдите количество книг, которое можно разместить на дискете


sym_s, lines, pages = 24, 50, 100
byte, kbyte = 4, 1024
cap = 1.44
book = byte * sym_s * lines * pages
disc = cap * kbyte**2
shelf = int((disc // book))

print("Количество книг, помещающихся на дискету:", shelf)
