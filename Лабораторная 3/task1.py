class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, newname: str) -> str:
        raise AttributeError('Нельзя менять навание книги.')

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, newauthor: str) -> str:
        raise AttributeError('Нельзя менять автора книги.')

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, newpages: int) -> None:
        if not isinstance(newpages, int):
            raise TypeError("Количество страниц должно быть типа int.")
        if newpages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = newpages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    """ Класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, newduration: float) -> None:
        if not isinstance(newduration, float):
            raise TypeError("Продолжительность должна быть типа float.")
        if newduration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = newduration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
