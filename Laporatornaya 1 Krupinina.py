import doctest


class PiggyBank:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Копилка"

        :param capacity_volume: Объем копилки
        :param occupied_volume: Объем богатства

        Примеры:
        >>> piggy_bank = PiggyBank(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем копилки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество богатства должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество богатства не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_out_of_money(self) -> bool:
        """
        Функция которая проверяет является ли поросенок пустым

        :return: Является ли пятачок пустым

        Примеры:
        >>> piggy_bank = PiggyBank(500, 0)
        >>> piggy_bank.is_out_of_money()
        """
        ...

    def add_money_to_bank(self, money: float) -> None:
        """
        Добавление денег в свинью.
        :param money: Объем добавляемого груза

        :raise ValueError: Если количество добавляемых денег превышает свободное место в копилке, то вызываем ошибку

        Примеры:
        >>> piggy_bank = PiggyBank(500, 0)
        >>> piggy_bank.add_money_to_bank(200)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Добавляемые деньги должны быть типа int или float")
        if money < 0:
            raise ValueError("Добавляемые деньги должны быть положительным числом")
        ...

    def take_money_from_bank(self, estimate_money: float) -> None:
        """
        Извлечение денег из коплики.

        :param estimate_money: Количество изымаемых денег
        :raise ValueError: Если берешь больше, чем есть, то возвращается ошибка.

        :return: Объем реального изымания

        Примеры:
        >>> piggy_bank = PiggyBank(500, 500)
        >>> piggy_bank.take_money_from_bank(200)
        """
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
