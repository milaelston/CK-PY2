import time
import doctest

if __name__ == "__main__":
    class Jewelry:
        """Базовый класс украшения."""
        def __init__(self, name: str, material: str, charms: int):
            """
            Создание и подготовка к работе объекта "Украшение".

            :param name: Название изделия, только для чтения
            :param material: Материал, из которого состоит изделие
            :param charms: Количество подвесок на изделии

            Пример:
            >>> jewerly_piece = Jewelry("Diamond rain", "silver", 20)
            """
            self._name = name  # только для чтения
            self.material = material
            self.charms = charms

        def __str__(self):
            """
            Метод, который возращает строковую версию объекта, удобную для чтения пользователем кода.

            :return: Строковая версия объекта

            Пример:
            >>> jewerly_piece = Jewelry("Diamond rain", "silver", 20)
            >>> print(jewerly_piece)
            Jewerly piece 'Diamond rain', made of silver, includes 20 charms.
            """
            return f"Jewerly piece '{self._name}', made of {self._material}, includes {self._charms} charms."

        def __repr__(self):
            """
            Метод, который возращает строку с формальным печатаемым представлением объекта.

            :return: Формальное строковое представление объекта

            Пример:
            >>> jewerly_piece = Jewelry("Diamond rain", "silver", 20)
            >>> print(repr(jewerly_piece))
            Jewelry(name='Diamond rain', material='silver', charms=20)
            """
            return f"{self.__class__.__name__}(name={self._name!r}, material={self._material!r}, charms={self._charms})"

        @property
        def name(self) -> str:
            return self._name

        @property
        def material(self):
            return self._material

        @material.setter
        def material(self, newmat: str) -> None:
            matlist = ['stainless steel', 'silver', 'plastic']
            if not isinstance(newmat, str):
                raise TypeError("Necklace material must be of str type")
            if matlist.count(newmat) == 0:
                raise ValueError("Necklace material is not legitimate")
            self._material = newmat

        @property
        def charms(self):
            return self._charms

        @charms.setter
        def charms(self, newnum: int) -> None:
            if not isinstance(newnum, int):
                raise TypeError("Number of charms must be of int type")
            if newnum < 0:
                raise ValueError("Number of charms must not be less than zero")
            self._charms = newnum

        def sell(self) -> None:
            """
            Метод, имитирующий работу с API онлайн-магазина по продаже украшений.

            :return: None

            Пример:
            >>> jewerly_piece = Jewelry("Diamond rain", "silver", 20)
            >>> jewerly_piece.sell()
            Processing...
            Processing...
            Processing...
            The item "Diamond rain" is now available on the web shop!
            """
            for i in range(3):
                print("Processing...")
                time.sleep(1)
            print(f'The item "{self._name}" is now available on the web shop!')

        def estimate_price(self) -> int:
            """
            Метод, рассчитывающий примерную цену украшения.

            :return: Примерная цена украшения

            Пример:
            >>> jewerly_piece = Jewelry("Diamond rain", "silver", 20)
            >>> jewerly_piece.estimate_price()
            900
            """
            price_dict = {'stainless steel': 300, 'silver': 400, 'plastic': 150, 'charm': 25}
            price = price_dict[self._material] + self._charms*price_dict["charm"]

            return price

    class Necklace(Jewelry):
        """Класс украшения – ожерелья."""
        def __init__(self, name: str, material: str, length: int, charms: int):
            """
            Создание и подготовка к работе объекта "Ожерелье". Конструктор расширен и включает в себя атрибут длины.

            :param name: Название ожерелья, только для чтения
            :param material: Материал, из которого состоит ожерелье
            :param length: Длина ожерелья в сантиметрах
            :param charms: Количество подвесок на ожерелье

            Пример:
            >>> old_necklace = Necklace("Night beauty", "silver", 42, 5)
            """
            super().__init__(name=name, material=material, charms=charms)
            self.length = length

        @property
        def length(self):
            return self._length

        @length.setter
        def length(self, newlen: int) -> None:
            if not isinstance(newlen, int):
                raise TypeError("Length of the necklace must be of int type")
            if newlen < 0:
                raise ValueError("Length of the necklace cannot be less than zero")
            if 0 < newlen < 1:
                raise ValueError("Length of the necklace must be expressed in centimeters")
            self._length = newlen

        def __str__(self):
            """
            Метод, который возращает строковую версию объекта, удобную для чтения пользователем кода.
            Перегружен, чтобы включать в себя атрибут длины ожерелья.

            :return: Строковая версия объекта

            Пример:
            >>> old_necklace = Necklace("Night beauty", "silver", 42, 5)
            >>> print(old_necklace)
            Necklace 'Night beauty', made of 42cm of silver, with 5 charms.
            """
            return f"Necklace '{self._name}', made of {self._length}cm of {self._material}, with {self._charms} charms."

        def __repr__(self):
            """
            Метод, который возращает строку с формальным печатаемым представлением объекта.
            Перегружен, чтобы включать в себя атбрибут длины ожерелья.

            :return: Формальное строковое представление объекта

            Пример:
            >>> old_necklace = Necklace("Night beauty", "silver", 42, 5)
            >>> print(repr(old_necklace))
            Necklace(name='Night beauty', material='silver', length=42, charms=5)
            """
            return f"{self.__class__.__name__}(name={self._name!r}, material={self._material!r}, length={self._length!r}, charms={self._charms})"

        # Метод "sell" унаследован

        def estimate_price(self) -> int:
            """
            Метод, рассчитывающий примерную цену украшения.
            Перегружен для учета длины ожерелья при расчете цены и включения нового прайс-листа.

            :return: Примерная цена украшения

            Пример:
            >>> old_necklace = Necklace("Night beauty", "silver", 42, 5)
            >>> old_necklace.estimate_price()
            486
            """
            price_dict = {'stainless steel': 350, 'silver': 400, 'plastic': 100, 'charm': 30}
            length_coeff = self._length / 50
            price = round(price_dict[self._material]*length_coeff + self._charms*price_dict["charm"])

            return price

    # все примеры вызова внутри документации
    doctest.testmod()
    pass
