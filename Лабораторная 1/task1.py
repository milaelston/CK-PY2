import doctest


class Pet:
    def __init__(self, name: str, appointment: int):
        """
        Создание и подготовка к работе объекта "Питомец"

        :param name: Имя домашнего питомца
        :param appointment: Дата приема питомца

        Пример:
        >>> pet1 = Pet("Rex", 20221231) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя питомца должен быть типа str")
        if name == "":
            raise ValueError("Имя питомца не может быть пустой строкой")
        self.name = name

        if not isinstance(appointment, int):
            raise TypeError("Дата приема должна быть записана числом типа int")
        if appointment < 20150101:
            raise ValueError("Дата приема должна быть записана в формате YYYYMMDD не раньше 2015 года")
        self.appointment = appointment

    def has_appointment(self) -> bool:
        """
        Функция, которая проверяет, есть ли у питомца прием у ветеринара в будущем

        :return: Есть ли прием (True - да, False - нет)

        Пример:
        >>> pet1 = Pet("Rex", 20221231)
        >>> pet1.has_appointment()
        """
        ...

    def change_appointment(self, newdate: int) -> None:
        """
        Функция, которая изменяет дату приема

        :param newdate: Новая дата приема

        :raise ValueError: Если дата введена некорректно, вызывается ошибка
        :raise TypeError: Если дата некорректного типа, вызывается ошибка

        Пример:
        >>> pet1 = Pet("Rex", 20221231)
        >>> pet1.change_appointment(20230101)
        """
        ...


class Iceberg:
    def __init__(self, height: int, length: int, shape: str):
        """
        Создание и подготовка к работе объекта "Айсберг"

        :param height: Высота айсберга
        :param length: Длина айсберга
        :param shape: Форма айсберга

        Пример:
        >>> ice1 = Iceberg(15, 59, "Dome")
        """
        if not isinstance(height, int):
            raise TypeError("Высота айсберга должна быть типа int")
        if height < 0:
            raise ValueError("Высота айсберга не может быть меньше нуля")
        self.height = height

        if not isinstance(length, int):
            raise TypeError("Длина айсберга должна быть типа int")
        if length < 0:
            raise ValueError("Длина айсберга не может быть меньше нуля")
        self.length = length

        if not isinstance(shape, str):
            raise TypeError("Форма айсберга должна быть типа str")
        self.shape = shape

    def classify_size(self) -> str:
        """
        Функция, которая возращает категорию размера айсберга

        :return: Название категории (Growler, Bergy Bit, Small, Medium, Large или Very Large)

        Пример:
        >>> ice1 = Iceberg(15, 59, "Dome")
        >>> ice1.classify_size()
        """
        ...

    def estimate_underwater(self) -> int:
        """
        Функция, которая рассчитывает примерные размеры подводной части айсберга

        :return: Объем подводной части айсберга

        Пример:
        >>> ice1 = Iceberg(15, 59, "Dome")
        >>> ice1.estimate_underwater()
        """
        ...

    def titanic(self, cutdown: int) -> None:
        """
        Функция, которая сокращает высоту надводной части айсберга на заданное значение

        :param cutdown: Количество метров, на которое сокращается высота айсберга
        :raise TypeError: Если заданное значение не типа int, вызывается ошибка
        :raise ValueError: Если заданное значение больше высоты айсберга, вызывается ошибка

        Пример:
        >>> ice1 = Iceberg(15, 59, "Dome")
        >>> ice1.titanic(50)
        """
        ...


class Church:
    def __init__(self, name: str, parishioners: int, employees: list):
        """
        Создание и подготовка к работе объекта "Церковь"

        :param name: Название церкви
        :param parishioners: Количество прихожан
        :param employees: Список работников

        Пример:
        >>> church1 = Church("Пресвятой Богородицы", 89, ["Алексей", "Игорь", "Евгения"])
        """
        if not isinstance(name, str):
            raise TypeError("Название церкви должно быть типа str")
        if name == '':
            raise ValueError("Название церкви не может быть пустой строкой")
        self.name = name

        if not isinstance(parishioners, int):
            raise TypeError("Количество прихожан должно быть типа int")
        if parishioners < 0:
            raise ValueError("Количество прихожан не может быть меньше нуля")
        self.parishioners = parishioners

        if not isinstance(employees, list):
            raise TypeError("Список работников должен быть типа list")
        self.employees = employees

    def update_parishioners(self, number: int) -> None:
        """
        Функция, которая обновляет количество прихожан

        :param number: Добавляемое или вычитаемое (с минусом) количество прихожан
        :raise TypeError: Если number не типа int, возвращается ошибка
        :raise ValueError: Если вычитаемое число больше количества прихожан по модулю, вызывается ошибка

        Пример:
        >>> church1 = Church("Пресвятой Богородицы", 89, ["Алексей", "Игорь", "Евгения"])
        >>> church1.update_parishioners(-2)
        """
        ...

    def sort_employees(self) -> None:
        """
        Функция, которая сортирует список работников по алфавиту

        Пример:
        >>> church1 = Church("Пресвятой Богородицы", 89, ["Алексей", "Игорь", "Евгения"])
        >>> church1.sort_employees()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
