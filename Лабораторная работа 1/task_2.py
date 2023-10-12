# TODO Найдите количество книг, которое можно разместить на дискете
CHAR_SIZE = 4                   # Размер одного символа в байтах

floppyCapacitySpaceMb = 1.44    # Объем дискеты в Мб
bookPageCount = 100             # Количество страниц в книге
linesPerPage = 50               # Число строк на странице
charactersInLine = 25           # Количество символов в строке

charactersInBook = bookPageCount * linesPerPage * charactersInLine  # Количество симовлов в книге

bookSizeBytes = charactersInBook * CHAR_SIZE                # Размер книги в байтах
floppyCapacitySpaceBytes = floppyCapacitySpaceMb*1024*1024  # Объем дискеты в байтах

bookOnFloppy = int(floppyCapacitySpaceBytes / bookSizeBytes)

print("Количество книг, помещающихся на дискету:", bookOnFloppy)
