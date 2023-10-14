# TODO Найдите количество книг, которое можно разместить на дискете
CHAR_SIZE = 4                       # Размер одного символа в байтах

floppy_capacity_space_mb = 1.44     # Объем дискеты в Мб
book_page_count = 100               # Количество страниц в книге
lines_per_page = 50                 # Число строк на странице
characters_in_line = 25             # Количество символов в строке

characters_in_book = book_page_count * lines_per_page * characters_in_line  # Количество симовлов в книге

book_size_bytes = characters_in_book * CHAR_SIZE                        # Размер книги в байтах
floppy_capacity_space_bytes = floppy_capacity_space_mb * 1024 * 1024    # Объем дискеты в байтах

book_on_floppy = int(floppy_capacity_space_bytes / book_size_bytes)

print("Количество книг, помещающихся на дискету:", book_on_floppy)
