import doctest


class Car:
    """
    Класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, mileage: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param mileage: Пробег автомобиля.

        :raise ValueError: Если пробег меньше нуля, то вызываем ошибку

        Примеры:
        >>> car = Car('Toyota', 2000)
        """
        self.brand = brand

        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным числом")
        self.mileage = mileage

    def drive(self, distance: int) -> None:
        """
        Езда на автомобиле.

        :param distance: Пройденное расстояние

        :raise ValueError: Если пройденное расстояние меньше нуля, то вызываем ошибку

        Примеры:
        >>> car = Car('Toyota', 5000)
        >>> car.drive(100)
        """
        if not isinstance(distance, int):
            raise TypeError("Пройденное расстояние должно быть типа int")
        if distance < 0:
            raise ValueError("Пройденное расстояние не может быть отрицательным числом")
        self.mileage += distance

    def print_info(self) -> None:
        """
        Получение информации об автомобиле.

        Примеры:
        >>> car = Car('Toyota', 900)
        >>> car.print_info()
        Toyota пробег 900 км
        """
        print(f'{self.brand} пробег {self.mileage} км')


class Smartphone:
    """
    Класс, описывающий смартфон.
    """

    def __init__(self, brand: str, battery_percentage: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param battery_percentage: Уровень заряда батареи

        :raise ValueError: Если уровень заряда выходит за диапазон значений от 0 до 100, то вызываем ошибку

        Примеры:
        >>> phone = Smartphone("Samsung", 90)
        """
        self.brand = brand

        if not isinstance(battery_percentage, int):
            raise TypeError("Уровень заряда батареи должен быть типа int")
        if not (0 < battery_percentage <= 100):
            raise ValueError("Уровень заряда батареи должен быть от 0 до 100")
        self.battery_percentage = battery_percentage

    def make_call(self, contact: str, duration: int) -> None:
        """
        Осуществление звонка смартфоном.

        :param contact: Имя контакта
        :param duration: Продолжительность звонка в секундах

        :raise ValueError: Если продолжительность звонка меньше 0, то вызывается ошибка

        Примеры:
        >>> phone = Smartphone("Samsung", 20)
        >>> phone.make_call("Ivan Petrov", 260)
        """
        if not isinstance(duration, int):
            raise TypeError("Продолжительность звонка должна быть типа int")
        if duration < 0:
            raise ValueError("Продолжительность звонка не может быть отрицательным числом")
        ...

    def charge(self, charging_percentage: int) -> None:
        """
        Зарядка батареи смартфона.

        :param charging_percentage: Количество заряда для добавления

        :raise ValueError: Если количество добавляемого заряда превышает 100, то вызывается ошибка
        :raise ValueError: Если количество добавляемого заряда меньше 0, то вызывается ошибка

        Примеры:
        >>> phone = Smartphone("Samsung", 50)
        >>> phone.charge(20)
        """

        if not isinstance(charging_percentage, int):
            raise TypeError("Зарядка батареи должен быть типа int")
        if (charging_percentage + self.battery_percentage) > 100:
            raise ValueError("Зарядка батареи не может превышать максимальное значение заряда батареи")
        if charging_percentage < 0:
            raise ValueError("Зарядка батареи не может быть отрицательным числом")
        ...


class Book:
    """
    Класс, описывающий книгу.
    """

    def __init__(self, title: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param pages: Количество страниц в книге

        :raise ValueError: Если количество страниц в книге меньше 1, то вызывается ошибка

        Примеры:
        >>> book = Book("Портрет", 120)
        """
        self.title = title

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 1:
            raise ValueError("Количество страниц не может быть меньше 1")
        self.pages = pages

    def open_book(self, page_number: int) -> None:
        """
        Открытие книги на указанной странице.

        :param page_number: Номер страницы для открытия

        :raise ValueError: Если номер страницы выходит за диапазон от 1 до количества страниц в книге, вызывается ошибка

        Примеры:
        >>> book = Book("Руслан и Людмила", 300)
        >>> book.open_book(50)
        """
        if not isinstance(page_number, int):
            raise TypeError("Количество страниц должно быть типа int")
        if not 1 < page_number <= self.pages:
            raise ValueError(f'Номер страницы должен быть в диапазоне от 1 до {self.pages}')
        ...

    def get_info(self) -> str:
        """
        Получение информации о книге.

        :return: Информация о книге

        Примеры:
        >>> book = Book("Мёртвые души", 300)
        >>> book.get_info()
        'Мёртвые души - 300 стр.'
        """
        return f'{self.title} - {self.pages} стр.'


if __name__ == "__main__":
    doctest.testmod()
    pass
